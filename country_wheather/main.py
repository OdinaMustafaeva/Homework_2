import json
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton, ttk

wn = tk.Tk()
# Window style
wn.title("weather")
wn.geometry("400x800")
wn.configure(bg='skyblue')


# Show weather
def show_weather():
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={select_city_combobox.get()}&apikey=CquPBJVd8ethk04ibQ97XOP7Kg6HLKMd"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    for s in range(5):
        day = response.json()['timelines']['daily'][s]['time']
        day_label = Label(wn, text=day[0:10], fg='blue', bg='white')
        day_label.grid(row=4+s, column=0)
        for i in range(len(response.json()['timelines']['hourly'])):
            h = response.json()['timelines']['hourly'][i]['time']
            day_label = Label(wn,
                              text=f"{h[12:16]} = {response.json()['timelines']['hourly'][i]['values']['temperature']}",
                              fg='green', bg='skyblue')
            day_label.grid(row=4+s, column=i+1)


weather_text_label = Label(wn, text='Weather application', fg='White', bg='skyblue', font=(26))
weather_text_label.grid(row=0, column=4)

# Select city Label
select_city_label = Label(text="Select city", fg='blue', bg='skyblue', font=(10))
select_city_label.grid(row=2, column=0)

# Select city combobox
url_country = 'https://restcountries.com/v3.1/all'
country = []
resp = requests.get(url_country)
for i in range(len(resp.json())):
    country.append(resp.json()[i]['name']['common'])
select_city_combobox = ttk.Combobox(wn, values=country, width=10)
select_city_combobox.grid(row=2, column=3)

# Show button
show_button = Button(text='Show', bg='yellow', fg='black', width=5, command=show_weather)
show_button.grid(row=3, column=0, pady=20)

if __name__ == '__main__':
    wn.mainloop()
