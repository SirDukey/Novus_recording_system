import schedule
from time import sleep
import subprocess as sp



def job():
    print("I'm working...")

schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    sleep(1)