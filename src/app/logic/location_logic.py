import os
import requests
from dotenv import load_dotenv

class LocationLogic:
    def __init__(self):
        """Initializes the LocationLogic with an API key."""

        load_dotenv()
        
        self.api_key = os.getenv('GEOAPIFY_API_KEY')

        if self.api_key is None:
            raise ValueError("API key not found. Please check your .env file.")

    def get_location_coordinates(self, location):
        """
        Get latitude and longitude of a location using Geoapify API.

        Parameters:
        location (str): The location to get coordinates for.

        Returns:
        dict: A dictionary containing the latitude and longitude of the location,
              or an error message if the location is not found or the request fails.
        """

        url = f"https://api.geoapify.com/v1/geocode/search?text={location}&apiKey={self.api_key}"
        
        try:
            response = requests.get(url)
            data = response.json()
             # Check if the request was successful and the location was found
            if response.status_code == 200 and 'features' in data and len(data['features']) > 0:
                # Extract coordinates
                coordinates = data['features'][0]['geometry']['coordinates']
                return {
                    "longitude": coordinates[0],
                    "latitude": coordinates[1]
                }
            else:
                return {"error": "Location not found"}
        
        except requests.exceptions.RequestException as e:
            # Handle request exceptions, such as network issues
            return {"error": f"Request failed: {str(e)}"}
