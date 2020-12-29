import os
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

def job():
	#execute main.py
	os.system('python main.py')

#schedule a job to re-execute the main.py script at a specific time.
scheduler = BackgroundScheduler(daemon = True)
scheduler.add_job(job, 'interval', minutes= 10)
scheduler.start()


app = Flask(__name__)

if __name__ == '__main__':
	app.run()