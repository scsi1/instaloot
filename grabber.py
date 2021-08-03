import os 
from termcolor import colored
import schedule
import time
import datetime
import os
import shutil
import random


profiles = ["pubity", "totally", "epicfunnypage", "scoobydoofruitsnacks", "schoolstweet", "meme.ig", "ight", "memezar", "memes"]
f_profiles = ["pubity, ", "totally, ", "epicfunnypage, ", "scoobydoofruitsnacks, ", "schoolstweet, ", "meme.ig, ", "ight, ", "memezar, ", "memes, "]
count = 20
DAILY_SCHEDULED_TIME = "6:00"


def routine():
    t_end = time.time() + 60 * 5
    
    while time.time() < t_end:
        profile = random.choice(profiles)
        print(colored(f"\nFetching from: {profile}\n"))
        os.system(f"instaloader {profile} --no-video-thumbnails --no-captions --no-metadata-json --no-compress-json --no-profile-pic --count={count} --dirname-pattern={os.getcwd()}\\media\\")
        print(colored(f"\nDone! Fetched {count} files from {profile}\n\n"))

def attemptRoutine():
    while(1):
        try:
            routine()
            break
        except OSError as err:
            print("Routine Failed on " + "OS error: {0}".format(err))
            time.sleep(60*60)

#attemptRoutine()
schedule.every().day.at("06:00").do(attemptRoutine)

attemptRoutine()
while True:
    schedule.run_pending()  
    time.sleep(60) # wait one min