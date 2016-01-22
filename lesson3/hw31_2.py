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
    for assignment in doc['scores']:
        if (assignment['type'] == "homework" and assignment['score'] < lowscore):
            lowscore = assignment['score']
    scores_out = [ assignment for assignment in doc['scores'] if (!(assignment['type'] == "homework" and assignment['score'] == lowscore)) ]
    result = grades.update_one({'_id':doc['_id']}, {'$set':{'scores': scores_out}})
