# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:18:47 2021

@author: Ashit Agarwal
"""

import requests
from datetime import date
import re
import os
import time

#Gets the last chat id so it can be used later to send message 
def getLastChatId():
    updates = "https://api.telegram.org/bot{}/getUpdates".format(token)
    response = requests.get(updates)
    response = response.json()
    last_update = len(response["result"]) - 1 
    chat_id = response["result"][last_update]["message"]["chat"]["id"]
    return str(chat_id)
    
#Function to send message to Telegram Bot
#@param: bot_message: Contains the message to be sent
def telegramBotSendText(bot_message):
     send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
     response = requests.get(send_text)
     return response.json()

#Gets the pincode from users and checks if valid or not
#@returns: returns pincode entered
def getPincode():
    correct = False
    while correct == False :
        pincode = input("Enter Pincode\n")
        correct = bool(re.match("^[1-9][0-9]{5}$", str(pincode)))
        if correct == True:
            return pincode

#Gets current date
#@return : returns date today
def getCurrentDate():
    dateToday = date.today()
    dateToday = dateToday.strftime("%d-%m-%Y")
    return dateToday

#Gets the Centers data for the entered pincode and date
#@params : pincode: pincode of the area to be looked for.
#@params : dateToday: the current date
#@returns : returns the data received if present other returns empty string
def getRequest(pincode, dateToday):
    sampleUserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, dateToday)
    headers = {'accept': 'application/json','Accept-Language': 'hi_IN', 'User-Agent': sampleUserAgent}
    proxy = {"http":"http://116.202.183.54:2223"}
    response = requests.get(url, headers=headers, proxies=proxy)
    
    
    if response.status_code == 200:
        result = response.json()
        result = result['centers']
        return result
    else:
        telegramBotSendText("Error Encountered")
        print(response.text)
        return ""
    
#Finds the center that have vaccines and calls printSessionsAvailable() funtion
#to send the centers with vaccine
#@param: result: Contains data of all the centers for the pincode
def showResults(result):
    centerCount = len(result)
    totalCenterVaccineAvailableAt = 0
    for i in range(centerCount):
        nameOfCenter = result[i].get("name")
        sessions = result[i].get("sessions")
        sessions = list(filter(lambda x: x.get("available_capacity") > 0, sessions))
        sessionsCount = len(sessions)
        if(sessionsCount > 0):
            telegramBotSendText(nameOfCenter)
            totalCenterVaccineAvailableAt += 1
            printSessionsAvailable(sessions, sessionsCount)

    if totalCenterVaccineAvailableAt == 0 :
        telegramBotSendText("All slots are booked")
        
#Sends available vaccine count message to Telegram
def printSessionsAvailable(sessions, sessionsCount):
     for i in range(sessionsCount):
            vaccineAvailable = sessions[i].get("available_capacity")
            dateAvailable = sessions[i].get("date")
            ageLimit = sessions[i].get("min_age_limit")
            if(vaccineAvailable > 0 ):
                message = "On Date {} vaccines available are {} for age {}+".format(dateAvailable,vaccineAvailable, ageLimit)
                telegramBotSendText(message)

token = os.environ.get('bot_token')

while True:
    bot_chatID = os.environ.get('ashit')

    pincode = 110001
    #pincode = getPincode()
    dateToday = getCurrentDate()
    telegramBotSendText("Get 7 days covid vaccination data from {}".format(dateToday))
    result = getRequest(pincode, dateToday)
    
    if len(result)>0:
        showResults(result)
    else:
        telegramBotSendText("No Center Available")
        
    time.sleep(10)