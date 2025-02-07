# FastAPI sample excercise
Quick example of a FastAPI app with an endpoint that can calculate the great circle distance between pairs of coordinates.
## Install with poetry
`poetry install`
## Run the app
`poetry run fastapi app.py`
## Forward localhost with NGROK using the same port as defined with FastAPI
`ngrok http http://localhost:8000`
## Test the haversine endpoint with e.g. curl on localhost
`curl --header "Content-Type: application/json" --data '{"x1":[5.0], "y1":[10.0], "x2": [6.0], "y2": [11.0]}'  http://localhost:8000/haversine`

You can use multiple coordinates as well in the body:

`{
    "x1": [5.0, 7.0],
    "y1": [10.0, 64.0],
    "x2": [6.0, 7.0],
    "y2": [11.0, 12.0]
}`

And the result should look like:

`{
    "results": {
        "0": 157.06653560698433,
        "1": 5742.27922210264
    }
}`

## Test the ChatGPT 4-o mini endpoint with a JSON payload
Use a `msg` field with a string value of max. 120 character length:
`curl --header "Content-Type: application/json" --data '{"msg": "Let me know if you can read this."}'  http://localhost:8000/chatbot`