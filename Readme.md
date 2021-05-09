# Vaccine-Availabilty
Python script to let you know the available vaccine slots on Cowin platform.
There are 3 scripts *VaccineCountToTG.py*, *VaccineCommandLinePincode.py* and *VaccineCountNormal.py*. 
If you want updates on a bot in Telegram use *VaccineCountToTG.py* otherwise use *VaccineCountNormal.py* or *VaccineCommandLinePincode.py*

## Installation(For VaccineCountNormal.py and VaccineCommandLinePincode.py )
```bash
pip install requests
```
## Installation(For VaccineCountToTG.py)

Requires Python.
Packages required could be found in requirement.txt
You only need *python-dotenv* if you are going to use VaccineCountToTG.py.

```bash
pip install python-dotenv
pip install requests
```
To send messages to the Telegram Bot, set the environment variable. example.env contains the required format. Your Bot token is required in the .env file.
Bot token is generated when you create your bot. Guide for setting up Telegram Bot to receive messages can be found at https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

## Usage(For VaccineCountToTG.py and VaccineCountNormal.py)

Change value of "pincode" variable to your desired pincode or you could uncomment #pincode = getPincode() line so as to ask for pincode on runtime.

## Execution
Run it like you would normally run a python script.
For VaccineCountToTG.py and VaccineCountNormal.py
```bash
python VaccineCountNormal.py
```
Or
```bash
python VaccineCountToTG.py
```

For VaccineCommandLinePincode.py

```bash
python VaccineCountToTG.py (your pincode here)
```
