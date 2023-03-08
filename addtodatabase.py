
# Importing Module We Need 

import checkinternet as ch
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# import warnings

# Intialize the Firebase Datebase 

cred = credentials.Certificate("serviceKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL" : "https://icore-attendence-system-default-rtdb.firebaseio.com/"
})

# Assign the Variable

active = ch.is_connect()

data = {
    "355652" :
    {
        "Name" : "SanthaKumar",
        "Dept": "Human Resoure",
        "Starting_year":2018,
        "Total_Attendance":4,
        "Standing" :"6",
        "Total_Year":4,
        "Last_Attendance":"2023-03-01 00:30:20"
    },
      "852741" :
    {
        "Name" : "Sam Ramesh",
        "Dept": "Devolping Department",
        "Starting_year":2020,
        "Total_Attendance":6,
        "Standing" :"6",
        "Total_Year":2,
        "Last_Attendance":"2022-03-01 00:30:20"
    },
      "963852" :
    {
        "Name" : "Elon Musk",
        "Dept": "Mangement",
        "Starting_year":2015,
        "Total_Attendance":6,
        "Standing" :"6",
        "Total_Year":6,
        "Last_Attendance":"2022-03-01 00:30:20"
    } 
}

# Create Employee Directory into Store Data of Employee Details

if active:
    ref = db.reference("Employee")
    for key,value in data.items():
        ref.child(key).set(value)
    print(" Data Stored in Database , Successfully..")
else:
    print(" This required Internet Connection")
    print(" Please Turn ON Internet Connection ")
    