import time
import sys
import json
fn = 'users.json'


class adminTools:
    data = {}

    def __init__(self):
        self.load()
        print(self.data)

    def load(self):
        with open(fn) as f:
            self.data = json.load(f)

    def write(self):
        with open(fn, 'w') as f:
            json.dump(self.data, f)

    def addUser(self, name):
        self.load()
        self.data[name] = {"Jobs": []}
        self.write()

    def addJob(self):
        self.load()
        job = input("Give a name for the job\n")
        frequency = 7
        try:
            frequency = int(input(
                "How frequent is this job required (Give a number of days)\n"))
        except:
            print("Please input an integer")
            sys.exit(1)
        for i in self.data:
            newJob = dict()
            newJob['name'] = job
            newJob['frequency'] = frequency
            start = 0
            try:
                start = int(input(
                    "How many days from now does the job start? for " + i + "\n"
                ))
            except:
                print("Please input an integer")
                sys.exit(1)
            newJob['nextOccurance'] = int(time.time()) + start*3600*24
            try:
                self.data[i]['Jobs'].append(newJob)
                self.write()
            except KeyError:
                jobs = list()
                jobs.append(newJob)
                self.data[i]['Jobs'] = jobs
                self.write()
