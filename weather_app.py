
class WeatherDataFetcher():
    def fetch_weather_data(current_city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {current_city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(current_city, {})
    
class WeatherDataParser():
    def parse_weather_data(weather_data):
        # Function to parse weather data
        if not weather_data:
            return "Weather data not available"
        current_city = weather_data["city"]
        temperature = weather_data["temperature"]
        condition = weather_data["condition"]
        humidity = weather_data["humidity"]
        return f"Weather in {current_city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class Forecast(WeatherDataFetcher,WeatherDataParser):
    def get_detailed_forecast(current_city):
        # Function to provide a detailed weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(current_city)
        return WeatherDataParser.parse_weather_data(data)

    def display_weather(current_city):
        # Function to display the basic weather forecast for a city
        weather_data = WeatherDataFetcher.fetch_weather_data(current_city)
        if not weather_data:
            return f"Weather data not available for {current_city}"
        else:
            weather_report = WeatherDataParser.parse_weather_data(weather_data)
            return weather_report

class UserInterface(Forecast):

    def interface(self):
        while True:
            current_city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if current_city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = Forecast.get_detailed_forecast(current_city)
            else:
                forecast = Forecast.display_weather(current_city)
            print(forecast)
            

if __name__ == "__main__":
    main_interface = UserInterface().interface()
    