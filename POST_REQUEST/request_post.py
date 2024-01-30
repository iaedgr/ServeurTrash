import requests
import json  # Add json module for JSON parsing

url = "https://imanedgr.pythonanywhere.com/"

file_path = "glass206.jpg"

with open(file_path, "rb") as file:
    files = {"file": (file_path, file)}
    response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    response_json = json.loads(response.text)
    final_result = response_json.get("result")
    if final_result is not None:
        print(final_result)
    else:
        print("Final result not found in the response JSON.")

else:
    print(f"Failed to upload file. Status code: {response.status_code}")
    print(response.text)