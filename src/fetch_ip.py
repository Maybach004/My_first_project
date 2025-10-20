import requests

response = requests.get("https://api.ipify.org?format=json", timeout=10)
print("Your public IP is:", response.json()["ip"])
