import requests

API_KEY = "49f447c835ea37ef53e8e8d1b4eaf542"
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

city = input("Enter city name: ")

# ---- Current Weather ----
current_request = f"{CURRENT_URL}?q={city}&appid={API_KEY}&units=metric"
current_response = requests.get(current_request)

if current_response.status_code == 200:
    current_data = current_response.json()
    print("\n--- Current Weather ---")
    print(f"Weather: {current_data['weather'][0]['description']}")
    print(f"Temperature: {current_data['main']['temp']}°C")
    print(f"Humidity: {current_data['main']['humidity']}%")
else:
    print("Error:", current_response.status_code, current_response.text)
    exit()


# ---- 5-Day Forecast ----
forecast_request = f"{FORECAST_URL}?q={city}&appid={API_KEY}&units=metric"
forecast_response = requests.get(forecast_request)

if forecast_response.status_code == 200:
    forecast_data = forecast_response.json()
    print("\n--- 5-Day Forecast ---")

    for item in forecast_data["list"][:10]:  # first 10 entries (~2 days)
        dt = item["dt_txt"]
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        print(f"{dt} -> {temp}°C, {desc}")
else:
    print("Forecast not available!")
