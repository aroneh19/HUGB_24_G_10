import os
import unittest
from unittest.mock import patch
import requests
from app.logic.location_logic import LocationLogic
from dotenv import load_dotenv

class TestLocationLogic(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.api_key = os.getenv('GEOAPIFY_API_KEY')
        self.location_logic = LocationLogic()

    @patch('requests.get')
    def test_get_location_coordinates_success(self, mock_get):
        # Mock the response from the Geoapify API
        mock_response = {
            "features": [
                {
                    "geometry": {
                        "coordinates": [-73.935242, 40.730610]  # Example coordinates for New York
                    }
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # Call the method with a test location
        result = self.location_logic.get_location_coordinates("New York")

        # Assert that the returned coordinates are correct
        self.assertEqual(result, {"longitude": -73.935242, "latitude": 40.730610})

    @patch('requests.get')
    def test_get_location_coordinates_not_found(self, mock_get):
        # Mock a response indicating the location was not found
        mock_response = {
            "features": []
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        result = self.location_logic.get_location_coordinates("Unknown Location")

        # Assert that the returned error message is correct
        self.assertEqual(result, {"error": "Location not found"})

    @patch('requests.get')
    def test_get_location_coordinates_request_exception(self, mock_get):
        # Simulate a request exception
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        result = self.location_logic.get_location_coordinates("New York")

        # Assert that the returned error message is correct
        self.assertEqual(result, {"error": "Request failed: Network error"})

if __name__ == '__main__':
    unittest.main()
