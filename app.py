from flask import Flask, request, Response

from .backend.airport import GetAirport

app = Flask(__name__)


@app.route("/airport", methods=["GET", "POST"])
def location():
    """This is an endpoint that will handle the GET and POST requests"""
    if request.method == "POST":
        request_data = request.get_json()
        try:
            user_lat = request_data["latitude"]
            user_lon = request_data["longitude"]
            if isinstance(user_lat, float) and isinstance(user_lon, float):
                airport_obj = GetAirport()
                airport_name = airport_obj.closest_airport(user_lat, user_lon)
                return Response(f"{airport_name}", status=200)
            else:
                return Response("Invalid latitude/longitude", status=400)
        except:
            return Response("Please provide the latitude and longitude", status=400)
    elif request.method == "GET":
        message = """<h1>Closest Airport</h1>
        <p>To find the closest airport to a location, 
        \nplease send a post request with the valid coordinates (latitude and longitude)</p>\n
        Sample post body:
        {
            "latitude": 52.2,
            "longitude": 0.9
        }"""
        return Response(message, status=200)
