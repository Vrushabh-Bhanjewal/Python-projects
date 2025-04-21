import tkinter as tk
from requests import *
import json

window=tk.Tk()
window.geometry('400x500')
window.title('Weather App')

f1=('Times New Roman',15)
API_KEY='4587a6c585565f8bb5f6fe7b9384c69b'
frame1=tk.Frame(window)
frame1.pack()

Title_label=tk.Label(frame1,text='Weather App',font=f1).grid(row=0,column=0,pady=20,columnspan=2)
city_label=tk.Label(frame1,text='Enter city Name').grid(row=1,column=0)
city=tk.Entry(frame1)
city.grid(row=1,column=1,padx=20)

def search_city():
    city_serach=city.get()
    if(not city_serach):
        return
    try:
        res=get(f'https://api.openweathermap.org/data/2.5/weather?q={city_serach}&appid={API_KEY}')
        data=res.json()
        # print(data)
    except:
        pass
    frame2=tk.LabelFrame(window,text=city_serach,padx=20,pady=20,font=f1)
    frame2.pack()
    celcius=data['main']['temp'] - 273.15
    tk.Label(frame2,text=f'Weather: {data['weather'][0]['main']}').pack()
    tk.Label(frame2,text=f'Weather Info: {data['weather'][0]['description']}').pack()
    tk.Label(frame2,text=f'Temp: {round(celcius,2)}').pack()
    tk.Label(frame2,text=f'Humidity: {data['main']['humidity']}').pack()
    tk.Label(frame2,text=f'Country Code: {data['sys']['country']}').pack()
    tk.Label(frame2,text=f'Longitude: {data['coord']['lon']}').pack()
    tk.Label(frame2,text=f'Latitude: {data['coord']['lat']}').pack()    

search=tk.Button(frame1,text='Search City',padx=10,command=search_city)
search.grid(rows=2,column=0,columnspan=2,pady=10)

window.mainloop()
