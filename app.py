import requests

print("Checking Internet...")

response = requests.get("https://google.com")
print("Status Code:", response.status_code)
