import csv
from geopy.distance import geodesic


class GetAirport:
    """This is the class that would calculate the closest airport based on the user entered coordinates"""

    def __init__(self):
        self.file_name = "uk_airport_coords.csv"

    def distance(self, airport_name, lat1, lon1, lat2, lon2):
        """Function to calculate the distance between two geographical points

        Args:
            airport_name (string): name of the airport
            lat1 (float): user entered latitude
            lon1 (float): user entered longitude
            lat2 (float): airport latitude
            lon2 (_type_): airport longitude

        Returns:
            distance (float): distance between the coordiantes
        """

        distance = geodesic((lat1, lon1), (lat2, lon2))
        print(f"{airport_name:20}{distance}")
        return distance

    def closest_airport(self, lat, lon):
        """Function to find the closest airport

        Args:
            lat (float): user entered latitude
            lon (float): user entered longitude

        Returns:
            airport_name (string): details of the closest airport
        """

        try:
            with open(self.file_name, "r") as f:
                reader = csv.reader(f)
                next(reader)
                min_dist = 100000
                for row in reader:
                    airport_lat = float(row[2])
                    airport_lon = float(row[3])
                    name = row[0]
                    dist = self.distance(name, lat, lon, airport_lat, airport_lon)
                    if dist < min_dist:
                        min_dist = dist
                        airport_name = f"Closest Airport details:\n Name: {row[0]} \n ICAO: {row[1]} \n Latitude: {row[2]} \n Longitude: {row[3]}"
                return airport_name
        except FileNotFoundError:
            return (f"\nFile name '{self.file_name}' not found\n")
