from tkinter import * 
import tkinter  as tk
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e10df5b0d9bc98d6cc71170391aa65f1").json()
    w_Label1.config(text=data["weather"][0]["main"])
    wb_Label1.config(text=data["weather"][0]["description"])
    temp_Label1.config(text=str(data["main"]["temp"]-273.15))
    per_Label1.config(text=data["main"]["pressure"])




win =tk.Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x600")


name_Label = tk.Label(win,text="Weather App",
                   font=("Time New Roman",40,"bold"))
name_Label.place(x=25,y=25,height=50,width=450)

city_name = StringVar()
list_name= [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa",
    "Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala",
    "Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
    "Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
    "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
]

com = ttk.Combobox(win,text="Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=125,height=50,width=450)








w_Label = tk.Label(win,text="Weather CLimate",
                   font=("Time New Roman",10))
w_Label.place(x=25,y=260,height=50,width=150)
w_Label1 = tk.Label(win,text="",
                   font=("Time New Roman",10))
w_Label1.place(x=250,y=260,height=50,width=150)


wb_Label = tk.Label(win,text="Weather Description",
                   font=("Time New Roman",10))
wb_Label.place(x=25,y=330,height=50,width=150)
wb_Label1 = tk.Label(win,text="",
                   font=("Time New Roman",10))
wb_Label1.place(x=250,y=330,height=50,width=150)



temp_Label = tk.Label(win,text="Temperature",
                   font=("Time New Roman",10))
temp_Label.place(x=25,y=400,height=50,width=150)
temp_Label1 = tk.Label(win,text="",
                   font=("Time New Roman",10))
temp_Label1.place(x=250,y=400,height=50,width=150)


per_Label = tk.Label(win,text="Pressure",
                   font=("Time New Roman",10))
per_Label.place(x=25,y=470,height=50,width=150)
per_Label1 = tk.Label(win,text="",
                   font=("Time New Roman",10))
per_Label1.place(x=250,y=470,height=50,width=150)




done_button =Button(win,text="Done",
                    font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190 ,height=50,width=100, )





win.mainloop()