import pymongo
import sys
#from pyspark import SparkConf, SparkContext

#conf = SparkConf().setMaster("local").setAppName("HW22")
#sc = SparkContext(conf = conf)

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

query = {'type':'homework'}
cur = grades.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

prev_id = ""
total_dels = 0
for doc in cur:
    if (doc['student_id'] != prev_id):
        id = doc['_id']
        try:
            grades.delete_one({'_id':id})
        except Exception as e:
            print "Exception: ", type(e), e
    prev_id = doc['student_id']
#print "total deleted: ", total_dels
