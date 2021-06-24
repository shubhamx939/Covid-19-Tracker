import tkinter as tk
from typing import Text
import requests 
import datetime


def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_recovered = str(json_data['recovered'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_recovered = str(json_data['todayRecovered'])
    today_deaths = str(json_data['todayDeaths'])
    active = str(json_data['active'])
    critical = str(json_data['critical'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    
    
    label.config(text="Total Cases: " + total_cases + "\n"
                 + "Total Recovered: " + today_recovered + "\n"
                 + "Total Deaths: " + today_deaths + "\n"
                 + "Today's Cases: " + today_cases + "\n"
                 + "Today's Recovered: " + today_recovered + "\n"
                 + "Today's Deaths: " + today_deaths + "\n"
                 + "Active Cases: " + active + "\n"
                 + "Critical Cases: " + critical)
    
    label2.config(text=date)
    

canvas = tk.Tk()
canvas.geometry("500x500")
canvas.title("Covid-19 Tracker")

f = ("roboto", 15)

button = tk.Button(canvas, font= f, text= "Load Data", command=getCovidData)
button.pack(pady=20)

label = tk.Label(canvas, font=f)
label.pack(pady=20)

label2 = tk.Label(canvas, font=8)
label2.pack()

getCovidData()

canvas.mainloop()
