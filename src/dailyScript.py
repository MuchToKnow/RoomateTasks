import pymongo
import schedule
import time
import copy
import PySimpleGUI as sg
import frontEnd

client = pymongo.MongoClient('localhost', 27017)
db = client.roommate
fe = frontEnd.fe()


def updateDisplay():
    """
    Main funcion called periodically
    Grabs current jobs from the db and updates FE and DB
    """
    epochTime = int(time.time())
    feRows = list()
    for user in db.users.find():
        print(user)
        jobs = list()
        try:
            jobs = user['jobs']
        except:
            print("User has no jobs")
        for idx in range(len(jobs)):
            job = jobs[idx]
            if(job['nextOccurance'] >= epochTime):
                # TODO: Put it on the FE table
                rowText = [user['name'], job['name']]
                row = [sg.Text(t, size=(16, 2)) for t in rowText]
                feRows.append(row)
                # Update the next time in the db
                updateJobs(user, job, user['jobs'], idx)
    fe.renderGUI(feRows)


def updateJobs(user, job, jobs, idx):
    """
    def updateJobs(user, job, jobs, idx):
    """
    nextOccurance = job['frequency'] * 3600 + int(time.time())
    newJob = copy.deepcopy(job)
    newJob['nextOccurance'] = nextOccurance
    newJobs = copy.deepcopy(jobs)
    newJobs[idx] = newJob
    db.users.update_one(filter={'_id': user['_id']}, update={
        '$set': {'jobs': newJobs}})


updateDisplay()
schedule.every().day.at('01:00').do(updateDisplay)
while True:
    schedule.run_pending()
    time.sleep(60)
