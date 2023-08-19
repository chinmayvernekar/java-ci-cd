import requests
import json

# Replace with your API endpoint URL
API_URL = "http://localhost:8080/"

# Replace with the expected JSON response as a dictionary
EXPECTED_RESPONSE = {"test": "HELLO WORLD"}

# Make the API request
try:
    response = requests.get(API_URL)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        actual_response = response.json()

        # Print the expected and actual responses for debugging
        print("Expected Response:")
        print(json.dumps(EXPECTED_RESPONSE, indent=2))

        print("Actual Response:")
        print(json.dumps(actual_response, indent=2))

        # Compare the responses
        if EXPECTED_RESPONSE == actual_response:
            print("API response matches the expected input.")
        else:
            print("API response does not match the expected input.")
            exit(1)
    else:
        print(f"API request failed with status code {response.status_code}")
        exit(1)

except requests.exceptions.RequestException as e:
    print(f"API request error: {e}")
    exit(1)
