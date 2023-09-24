import unittest
import json
from unittest.mock import patch, Mock
from get_company_data import analyze_company

class TestMyModule(unittest.TestCase):
    @patch('get_company_data.requests.get')
    def test_analyze_company_schema_and_confidence(self, mock_get):
        # Load data from the fake_company_data.json file
        with open('fake_company_data.json', 'r') as file:
            company_data = json.load(file)

        # Mock the response for an existing company with confidence score 0.9 (company_2)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = company_data['company_2']  # Use data for company_2
        mock_get.return_value = mock_response

        # Test for an existing company with a confidence score of 0.9
        result = analyze_company('company_2')
        self.assertEqual(result, "Analysis result for XYZ Ltd.")

        # Check schema keys for company_2
        self.assertIn("name", company_data['company_2'])
        self.assertIn("revenue", company_data['company_2'])
        self.assertIn("employees", company_data['company_2'])
        self.assertIn("industry", company_data['company_2'])
        self.assertIn("location", company_data['company_2'])
        self.assertIn("confidence_score", company_data['company_2'])
        self.assertIn("leadership", company_data['company_2'])
        self.assertIn("products", company_data['company_2'])

        # Check confidence score for company_2
        confidence_score = company_data['company_2']["confidence_score"]
        self.assertTrue(0.9 <= confidence_score <= 1, "Confidence score should be 0.9 or higher")

        # Mock the response for a non-existent company
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.side_effect = Exception("JSON decoding failed")
        mock_get.return_value = mock_response

        # Mock the response for an existing company with confidence score 0.8 (company_1)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = company_data['company_1']  # Use data for company_1
        mock_get.return_value = mock_response

        # Test for an existing company with confidence score 0.8
        with self.assertRaises(Exception) as context:
            analyze_company('company_1')
        self.assertIn("Company does not meet the confidence score threshold for analysis", str(context.exception))

if __name__ == '__main__':
    unittest.main()
