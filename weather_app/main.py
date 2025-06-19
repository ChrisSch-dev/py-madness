import requests

API = "https://wttr.in/{}?format=3"

def get_weather(location):
    resp = requests.get(API.format(location))
    return resp.text

def main():
    print("Weather App")
    location = input("Enter location (city or country): ")
    print(get_weather(location))

if __name__ == "__main__":
    main()