import os 
from termcolor import colored
import schedule
import time
import datetime
import shutil
import smtplib
from email.message import EmailMessage
from glob import glob
from os.path import join
import random
from twilio.rest import Client
import pyimgur
import base64
from base64 import b64encode
import requests, json

DAILY_SCHEDULED_TIME = "07:00"

account_sid = 'ACbab8fa866e1dbe1d0b8326b46d85659c'
auth_token = '349ccb76128918c8db9e7f0ee415571a'

def routine():
   files = os.listdir(f"c:\\Users\\scsii\\instagram\\media\\")
   for file in files:

        CLIENT_ID = "6b53fc1507cb0c1"
        headers = {f"Authorization": "Client-ID 6b53fc1507cb0c1"}

        url = "https://api.imgur.com/3/upload.json"

        j1 = requests.post(
            url, 
            headers = headers,
            data = {
                'image': b64encode(open(f"{os.getcwd()}//media//{file}", 'rb').read()),
                'type': 'base64',
                'name': f"{file}",
                'title': f"{file}"
            }
        )
        data = json.loads(j1.text)['data']; 
        if 'link' in data:
            print(data['link'])

            client = Client(account_sid, auth_token)
            imglink = data['link']
            message = client.messages \
            .create(
                messaging_service_sid='MG1c351fca39ee41d798ff763b7d9a2692',
                body=f'\n\nNew Meme!: {imglink}',
                to='+15067330746'
            )


def attemptRoutine():
    while(1):
        try:
            routine()
            break
        except OSError as err:
            print("Routine Failed on " + "OS error: {0}".format(err))
            time.sleep(60*60)

#attemptRoutine()
schedule.every().day.at(DAILY_SCHEDULED_TIME).do(attemptRoutine)

attemptRoutine()
while True:
    schedule.run_pending()  
    time.sleep(60) # wait one min