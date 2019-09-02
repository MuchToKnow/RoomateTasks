import pymongo
import time
import sys
client = pymongo.MongoClient('localhost', 27017)
db = client.roommate


class adminTools:

    def addUser(self, name):
        db.users.insert_one(document={'name': name})

    def addJob(self, name):
        user = db.users.find_one(filter={'name': name})
        name = input("Give a name for the job\n")
        frequency = 7
        try:
            frequency = int(input(
                "How frequent is this job required (Give a number of days)\n"))
        except:
            print("Please input an integer")
            sys.exit(1)
        newJob = dict()
        newJob['name'] = name
        newJob['frequency'] = frequency
        # TODO: Add time picker for start date
        newJob['nextOccurance'] = int(time.time()) + frequency*3600
        try:
            jobs = user['jobs']
            jobs.append(newJob)
            db.users.update_one(filter={'_id': user['_id']}, update={
                                '$set': {'jobs': jobs}})
        except KeyError:
            jobs = list()
            jobs.append(newJob)
            db.users.update_one(filter={'_id': user['_id']}, update={
                '$set': {'jobs': jobs}})
