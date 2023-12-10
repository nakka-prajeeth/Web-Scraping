import requests
import pandas as pd


class WeatherApi:
    """
    WeatherApi class for fetching weather data from the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key for accessing the OpenWeatherMap API.
        base_url (str): The base URL of the OpenWeatherMap API.

    Methods:
        __init__(self, api_key: str) -> None:
            Initializes a WeatherApi instance with the provided API key.

        getWeatherData(self, city: str) -> pd.DataFrame or None:
            Makes a request to the OpenWeatherMap API for weather data of the specified city.
            Returns the weather data as a Pandas DataFrame.

    """

    def __init__(self, apiKey: str) -> None:
        """
        Initializes a WeatherApi instance with the provided API key.

        Args:
            apiKey (str): The API key for accessing the OpenWeatherMap API.
        """
        self.apiKey = apiKey
        self.baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    def getWeatherData(self, city: str) -> pd.DataFrame or None:
        """
        Makes a request to the OpenWeatherMap API for weather data of the specified city.
        Returns the weather data as a Pandas DataFrame.

        Args:
            city (str): The name of the city for which weather data is requested.

        Returns:
            pd.DataFrame or None: Weather data as a Pandas DataFrame if successful, None if there is an error.
        """
        try:
            # Making a request to the OpenWeatherMap API
            params = {"q": city, "appid": self.apiKey}
            response = requests.get(self.baseUrl, params=params)

            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Extracting relevant weather information
                weatherInfo = {
                    "City": data["name"],
                    "Country": data["sys"]["country"],
                    "Temperature (Celsius)": data["main"]["temp"],
                    "Humidity (%)": data["main"]["humidity"],
                    "Weather Condition": data["weather"][0]["description"],
                }

                # Creating a DataFrame from the extracted information
                df = pd.DataFrame([weatherInfo])
                return df

            else:
                print(f"Error fetching weather data: {response.status_code}")
                return None

        except Exception as e:
            print(f"Error: {e}")
            return None
