# Vaccine-Availabilty
Python script to let you know the available vaccine slots on Cowin platform.
There are 3 scripts *VaccineCountToTG.py*, *VaccineCommandLinePincode.py* and *VaccineCountNormal.py*. 
If you want updates on a bot in Telegram use *VaccineCountToTG.py* otherwise use *VaccineCountNormal.py* or *VaccineCommandLinePincode.py*

## Installation(For VaccineCountNormal.py)
```bash
pip install requests
```
## Installation(For VaccineCountToTG.py and VaccineCommandLinePincodepy.py )

Requires Python.
Packages required could be found in requirement.txt
You only need *python-dotenv* if you are going to use VaccineCountToTG.py.

```bash
pip install python-dotenv
pip install requests
```
To send messages to the Telegram Bot, set the environment variable in the example.env. Put the bot token in it and rename example.env to just ".env".
Bot token is generated when you create your bot.

## Telegram Bot Creation
```bash
On Telegram, search @ BotFather, send him a “/start” message
Then send “/newbot” message, then follow the instructions to setup a name and a username
Your bot is now ready, be sure to save a backup of your API token, this API token is your bot_token
```
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
python VaccineCommandLinePincodepy.py (your pincode here)
```
