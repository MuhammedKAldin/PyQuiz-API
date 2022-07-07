import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10")

def requestJson(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(requestJson(response.json()["results"]))
print(x[0]["category"])