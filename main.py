import requests

def get_weather(city):
    # Free public weather API endpoint
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\nWeather Result: {response.text.strip()}\n")
        else:
            print("\nCould not fetch weather. Please try again.\n")
    except Exception as e:
        print(f"\nError connecting to service: {e}\n")

if __name__ == "__main__":
    print("=== Simple Weather Checker ===")
    user_city = input("Enter city name (e.g., London, Tokyo, Lagos): ")
    if user_city.strip():
        get_weather(user_city)
    else:
        print("City name cannot be empty.")
