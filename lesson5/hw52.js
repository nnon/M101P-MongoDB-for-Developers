use test
db.zips.aggregate([
    {$match:
       {
         'state' : { $in : ["CA", "NY"]},
       } 
    },
    {$group:
       {
         '_id' : {
                    'state' : "$state",
                    'city' : "$city"
                 },
         'pop' : {$sum : "$pop"}
       }
    },
    {$match:
       {
         'pop': {"$gt" : 25000}
       }
    },
    {$group:
       {
	 '_id' : 1, 
	 'avg_pop' : {$avg : "$pop"}
       }
    }
])


