use test
db.zips.aggregate([
   {$project: 
      {
         pop : 1,
	 first_char : {$substr : ["$city",0,1]},
      }	 
   },
   {$match:
      {
         first_char : { $regex : '[0-9]'}
      }
   },
   {$group:
      {
         _id : 1,
         pop : {$sum : "$pop"}
      }
   }
])
