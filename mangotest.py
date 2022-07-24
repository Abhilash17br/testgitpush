import pymongo
client = pymongo.MongoClient("mongodb+srv://root:fsds2022@abhilash.mdw9l.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"abhilash",
    "emailid":"abhilash17br@gmail.com",
    "surname":"br"
}

db1=client["mongotest"]
coll=db1['test']
coll.insert_one(d)

d={
    "name":"abhilash",
    "emailid":"abhilash17br@gmail.com",
    "surname":"br"
}

d={
    "name":"abhilash",
    "emailid":"abhilash17br@gmail.com",
    "surname":"br"
}

