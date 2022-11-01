# Solution: Technical task | L3Harris Flight Data Services
## Author: Muhammad Tauseef Raja
## Date: 24/10/2022

## Intro
I have developed the solution for this task in Python using the Geopy, CSV and Flask. This read me will guide you
on how to access the application. Used Flask to create an endpoint `/airport` that would accept GET and POST requests.
The closest airport to the valid latitude and longitude entered will be in the response of the a successful post request.

The distance finding script will also display the distance of each airport (from the csv file) to the posted latitude and
longitude.

## How to run the app
To run the app, simply `cd` into the main project directory `L3Harris Flight Data Services` and follow the following steps:
### Run the virtual environment
For this you have to have a Python library installed to create virtual environments like `virtualenv` (`pip install virtualenv`)
- `source airport-env/bin/activate`
### Install dependencies
Install the requirements:
- `pip install -r requirements.txt`
### Run Flask app
Run the following command to begin the flask app server locally:
- `flask run`
### Send a GET request
While the flask app is running, CMD, terminal or an api dev tool like postman or insomnia can be used.
#### From CMD/terminal:
- `curl -X GET http://127.0.0.1:5000/airport`
#### From browser window or api dev tool visit:
- `http://127.0.0.1:5000/airport`
### Send a POST request
Send a post request with the body consisting of the latitude and longitude:
#### From CMD/terminal:
- `curl -d '{"latitude": 52.2, "longitude": 0.9}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/airport`
#### From an api dev tool
Select POST as the method and post to:
- ` http://127.0.0.1:5000/airport`
sample post body looks like:
{
    "latitude": 52.2,
    "longitude": 0.9
}
(use any values for the latitude and longitude, 52.2 and 0.9 are example values)