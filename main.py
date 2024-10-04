import requests
from tkinter import *
from tkinter import messagebox
import os
from dotenv import load_dotenv


window = Tk()
window.title('Weather App')

city_label = Label(window, text='City: ')
city_label.pack()

city_entry = Entry(window)
city_entry.pack()

fetch_button = Button(window, text='Fetch')
fetch_button.pack()

weather_info_label = Label(window, text='')
weather_info_label.pack()

def fetch_weather():
    city = city_entry.get()
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    parameters = {
        'key': api_key,
        'q': city
    }
    url = 'http://api.weatherapi.com/v1/current.json'
    
    try:
        response = requests.get(url, params=parameters)
        data = response.json()
        temp = data['current']['temp_c']
        location = data['location']['country']
        weather_info_label.config(text=f"Temperature: {temp}°C\nWeather: {location}")
    except Exception:
          messagebox.showerror("Error", "Unable to fetch weather data")  

fetch_button.config(command=fetch_weather)

window.mainloop()