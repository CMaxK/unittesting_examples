# The below functions use the fake_company_data_json as fake data to mimic an API call. Often companies will provide
# sample of API outputs to specific endpoints on their websites. This strategy can be used in those example where
# you have a sample of an API output but do not have an access to their API yet.

import requests

def get_company_data(company_name):
    try:
        response = requests.get(f'https://api.example.com/companies/{company_name}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch company data: {e}")

def analyze_company(company_name):
    try:
        data = get_company_data(company_name)
        if not data:
            raise Exception("Company 'non_existent_company' not found in data")

        # Check if the confidence score is 0.9 or higher
        confidence_score = data.get("confidence_score", 0)  # Default to 0 if confidence_score is missing
        if confidence_score < 0.9:
            raise Exception("Company does not meet the confidence score threshold for analysis")

        # Check schema
        required_fields = ["name", "revenue", "employees", "industry", "location", "confidence_score"]
        for field in required_fields:
            if field not in data:
                raise Exception(f"Missing '{field}' in company data")

        # Perform further analysis on data below.......
        #
        #
        #

        return f"Analysis result for {data['name']}"

    except Exception as e:
        raise Exception(f"Failed to analyze company data: {e}")
