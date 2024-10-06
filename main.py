import requests
from tkinter import *
from tkinter import messagebox
import os
from dotenv import load_dotenv

# Initialize the main window
window = Tk()
window.title('Weather App')
window.geometry('400x300')  # Set the window size

# Define styles
window.config(bg='#2C3E50')  # Dark background

title_label = Label(window, text='Weather App', font=('Helvetica', 18, 'bold'), fg='white', bg='#2C3E50')
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# City label and entry
city_label = Label(window, text='Enter City:', font=('Helvetica', 12), fg='white', bg='#2C3E50')
city_label.grid(row=1, column=0, padx=20, pady=10, sticky='E')

city_entry = Entry(window, font=('Helvetica', 12), width=20)
city_entry.grid(row=1, column=1, padx=20, pady=10)

# Weather info label
weather_info_label = Label(window, text='', font=('Helvetica', 12), fg='white', bg='#2C3E50', justify=LEFT)
weather_info_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Fetch button
fetch_button = Button(window, text='Fetch Weather', font=('Helvetica', 12, 'bold'), bg='#1ABC9C', fg='white', width=20)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Function to fetch weather
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
        weather_info_label.config(text=f"Temperature: {temp}°C\nLocation: {location}")
    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather data")

# Set fetch button command
fetch_button.config(command=fetch_weather)

# Responsive layout configuration
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)


if __name__ == '__main__':
    window.mainloop()
