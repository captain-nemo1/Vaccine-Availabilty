# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:18:47 2021

@author: Administrator
"""

import requests
from datetime import date
import re
from dotenv import load_dotenv
import os

load_dotenv()

def get_last_chat_id_and_text():
    updates = "https://api.telegram.org/bot{}/getUpdates".format(token)
    global response
    response = requests.get(updates)
    response = response.json()
    last_update = len(response["result"]) - 1 
    chat_id = response["result"][last_update]["message"]["chat"]["id"]
    return str(chat_id)
    
def telegram_bot_sendtext(bot_message):
     send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
     response = requests.get(send_text)
     return response.json()


def getPincode():
    correct = False
    while correct == False :
        pincode = input("Enter Pincode\n")
        correct = bool(re.match("^[1-9][0-9]{5}$", str(pincode)))
        if correct == True:
            return pincode

def getCurrentDate():
    dateToday = date.today()
    dateToday = dateToday.strftime("%d-%m-%Y")
    return dateToday

def getRequest(pincode, dateToday):
    sampleUserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, dateToday)
    headers = {'accept': 'application/json','Accept-Language': 'hi_IN', 'User-Agent': sampleUserAgent}
    response = requests.get(url, headers=headers)
    
    
    if response.status_code == 200:
        result = response.json()
        result = result['centers']
        return result
    else:
        telegram_bot_sendtext("Error Encountered")
        return ""
    
def showResults(result):
    centerCount = len(result)
    totalCenterVaccineAvailableAt = 0
    for i in range(centerCount):
        nameOfCenter = result[i].get("name")
        sessions = result[i].get("sessions")
        sessions = list(filter(lambda x: x.get("available_capacity") > 0, sessions))
        sessionsCount = len(sessions)
        if(sessionsCount > 0):
            telegram_bot_sendtext(nameOfCenter)
            totalCenterVaccineAvailableAt += 1
            printSessionsAvailable(sessions, sessionsCount)

    if totalCenterVaccineAvailableAt == 0 :
        telegram_bot_sendtext("All slots are booked")
        
def printSessionsAvailable(sessions, sessionsCount):
     for i in range(sessionsCount):
            vaccineAvailable = sessions[i].get("available_capacity")
            dateAvailable = sessions[i].get("date")
            ageLimit = sessions[i].get("min_age_limit")
            if(vaccineAvailable > 0):
                message = "On Date {} vaccines available are {} for age {}+".format(dateAvailable,vaccineAvailable, ageLimit)
                telegram_bot_sendtext(message)

token = os.getenv('bot_token')
bot_chatID = get_last_chat_id_and_text()

pincode = 201005
#pincode = getPincode()
dateToday = getCurrentDate()
telegram_bot_sendtext("Get 7 days covid vaccination data from {}".format(dateToday))
result = getRequest(pincode, dateToday)

if len(result)>0:
    showResults(result)
else:
    telegram_bot_sendtext("No Center Available")