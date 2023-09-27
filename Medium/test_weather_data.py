import unittest
from unittest.mock import patch
from get_weather_data import analyze_weather

class TestGetWeatherData(unittest.TestCase):
    @patch('get_weather_data.requests.get')
    def test_analyze_weather_hot_dry(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'temperature': 30,
            'humidity': 60
        }
        result = analyze_weather('city')
        self.assertEqual(result, "Hot and dry")

    @patch('get_weather_data.requests.get')
    def test_analyze_weather_cold(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'temperature': 5,
            'humidity': 80
        }
        result = analyze_weather('city')
        self.assertEqual(result, "Cold")

    @patch('get_weather_data.requests.get')
    def test_analyze_weather_moderate(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'temperature': 20,
            'humidity': 50
        }
        result = analyze_weather('city')
        self.assertEqual(result, "Moderate")

    @patch('get_weather_data.requests.get')
    def test_analyze_weather_api_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception):
            analyze_weather('city')

if __name__ == '__main__':
    unittest.main()
