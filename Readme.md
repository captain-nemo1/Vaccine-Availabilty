# Vaccine-Availabilty
Python script to let you know the available vaccine slots on Cowin platform.
There are 2 scripts *VaccineCountToTG.py* and *VaccineCountNormal.py*.
If you want updates on a bot in Telegram use *VaccineCountToTG.py* otherwise use *VaccineCountNormal.py*

## Installation(For VaccineCountNormal.py)
No Special Steps is needed. Just run it normally.

## Installation(For VaccineCountToTG.py)

Requires Python.
Packages required could be found in requirement.txt
You only need *python-dotenv* if you are going to use VaccineCountToTG.py.

```bash
pip install python-dotenv
```
To send messages to the Telegram Bot, set the environment variable. example.env contains the required format. Your Bot token and Chat Id are required. 
Bot token is generated when you create your bot. And Chat id can be found by going to "https://api.telegram.org/bot(Your bot token)/getUpdates". Guide for setting up Telegram Bot to receive messages can be found at https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

## Usage

Change value of "pincode" variable to your desired pincode or you could uncomment #pincode = getPincode() line so as to ask for pincode on runtime.

## Execution
Run it like you would normally run a python script.




