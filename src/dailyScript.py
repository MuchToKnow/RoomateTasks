import schedule
import threading
import time
import copy
import PySimpleGUI as sg
import json
import frontEnd

fe = frontEnd.fe()
fn = 'users.json'
data = {}
with open(fn) as f:
    data = json.load(f)


def loadData():
    with open(fn) as f:
        data = json.load(f)


def writeData():
    with open(fn, 'w') as f:
        json.dump(data, f)


def updateDisplay():
    """
    Main funcion called periodically
    Grabs current jobs from the db and updates FE and DB
    """
    fe.close()
    epochTime = int(time.time())
    print(epochTime)
    feRows = list()
    for name, user in data.items():
        print(user)
        print(name)
        jobs = list()
        try:
            jobs = user['Jobs']
        except:
            print("User has no jobs")
        for idx in range(len(jobs)):
            job = jobs[idx]
            if(job['nextOccurance'] <= epochTime):
                # TODO: Put it on the FE table
                rowText = [name, job['name']]
                row = [sg.Text(t, size=(16, 2)) for t in rowText]
                feRows.append(row)
                # Update the next time in the db
                updateJobs(name, user, job, user['Jobs'], idx)
    fe.renderGUI(feRows)


def updateJobs(name, user, job, jobs, idx):
    """
    Updates the next occurance of the job in mongo
    """
    nextOccurance = job['frequency'] * 3600 * 24 + int(time.time())
    newJob = copy.deepcopy(job)
    newJob['nextOccurance'] = nextOccurance
    newJobs = copy.deepcopy(jobs)
    newJobs[idx] = newJob
    data[name]['Jobs'] = newJobs


schedule.every(7).days.do(updateDisplay)
while True:
    schedule.run_pending()
    time.sleep(60)
