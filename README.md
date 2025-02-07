# FastAPI sample excercise

## Install with poetry
`poetry install`
## Run the app
`poetry run fastapi app.py`
## Forward localhost with NGROK using the same port as defined with FastAPI
`ngrok http http://localhost:8000`
## Test endpoints with e.g. curl on localhost
`curl --header "Content-Type: application/json" --data '{"x1":[5.0], "y1":[10.0], "x2": [6.0], "y2": [11.0]}'  http://localhost:8000/haversine`