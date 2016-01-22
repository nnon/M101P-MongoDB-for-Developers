import pymongo
import sys
#from pyspark import SparkConf, SparkContext

#conf = SparkConf().setMaster("local").setAppName("HW22")
#sc = SparkContext(conf = conf)

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
grades = db.students

query = {'scores.type':'homework'}
cur = grades.find(query)

for doc in cur:
    lowscore = 100
    homework = []
    scores_out = []
    for assignment in doc['scores']:
        if (assignment['type'] == "homework"):
            if (assignment['score'] < lowscore):
                lowscore = assignment['score']
            homework.append(assignment)
        else:
            scores_out.append(assignment)
    for homework_assignment in homework:
        if (homework_assignment['score'] != lowscore):
            scores_out.append(homework_assignment)
    result = grades.update_one({'_id':doc['_id']}, {'$set':{'scores': scores_out}})
    #doc['scores'] = scores_out
    #assignment pop where homework and score
    #print doc['_id'], doc['name'], lowscore, doc['scores'] 
print result.matched_count
