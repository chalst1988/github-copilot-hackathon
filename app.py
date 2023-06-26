# import required modules
import requests, json
 
# Enter your API key here
api_key = "05c7cdf362f1087d15bbc60ff3b24659"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_forecast(city_name):
    # complete url address
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    #print(complete_url) 
    # return response object
    response = requests.get(complete_url) 
    # json method of response object
    # convert json format data into python format data
    x = response.json()
    #print("API Response: \n", x) 
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != 401:
        if x["cod"] != 404:
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
        
            # print data
            print(" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidity) +
                "\n description = " +
                            str(weather_description))
 
        else:
            print(" City Not Found ")
    else:
        print(x['message'])


if __name__ == "__main__":
    # Give city name
    city_name = input("Enter city name : ")
    get_weather_forecast(city_name)