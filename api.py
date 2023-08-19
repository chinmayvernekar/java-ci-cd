import requests
import json

# Replace with your API endpoint URL
API_URL = "http://localhost:8080/"

try:
    response = requests.get(API_URL)

    # Check for successful response (status code 200)
    if response.status_code == 200:
        try:
            actual_response = response.json()
            print("API Response:", actual_response)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print(f"API request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")
