import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Type definitions
longitude = Annotated[float, Field(ge=-180.0, le=180.0)]
latitude = Annotated[float, Field(ge=-90.0, le=90.0)]

class Coordinates(BaseModel):
    x1: list[longitude]
    y1: list[latitude]
    x2: list[longitude]
    y2: list[latitude]

# Routes
@app.get("/")
def root():
    return {"Hello": "Alexander"}

@app.post("/haversine")
async def haversine_distance(coordinates: Coordinates):
    """
    This endpoint calculates the distance between pairs of coordinates in kilometers
    Request body should contain a json in the form of:
    {"x1": [floats of coordinates],
     "y1": [floats of coordinates],
     "x2": [floats of coordinates],
     "y2": [floats of coordinates]}
    Lists should be equal in length
    """
    coordinate_df = pd.DataFrame(coordinates.model_dump())
    coordinate_df["haversine_distance"] = calculate_haversine_vectorized(df=coordinate_df)
    return {"results": coordinate_df["haversine_distance"]}


def calculate_haversine_vectorized(df: pd.DataFrame) -> pd.Series:
    """
    Haversine equation, see: https://en.wikipedia.org/wiki/Haversine_formula
    Double check results with: https://www.calculator.net/distance-calculator.html
    """
    x1, y1, x2, y2 = map(np.radians, [df.x1, df.y1, df.x2, df.y2])

    dy = y2 - y1
    dx = x2 - x1

    a = np.sin(dx / 2.0)**2 + np.cos(x1) * np.cos(x2) * np.sin(dy / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    distance = 6378.137 * c # earth radius to get results in km
    return distance
