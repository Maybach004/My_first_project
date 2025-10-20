import requests

def main():
    print("Hello, Maurice! This is your first organized Python project.")
    response = requests.get("https://api.ipify.org?format=json", timeout=10)
    print("Your public IP is:", response.json()["ip"])

if __name__ == "__main__":
    main()
import requests

def main():
    print("Hello, Maurice! This is your first organized Python project.")
    response = requests.get("https://api.ipify.org?format=json", timeout=10)
    print("Your public IP is:", response.json()["ip"])

if __name__ == "__main__":
    main()
