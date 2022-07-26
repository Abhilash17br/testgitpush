import pymongo

client = pymongo.MongoClient("mongodb+srv://root:fsds2022@abhilash.mdw9l.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client["inventory"]
collection=database['table']

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

#collection.insert_many(data)

"""
d=collection.find()
for i in d:
    print(i)

d=collection.find({ "status": "A"})
for i in d:
    print(i)

d=collection.find({ "status": {"$in":["A","P"]}})
for i in d:
    print(i)

d=collection.find({ "status": {"$gt":"C"}})
for i in d:
    print(i)

d = collection.find({"qty": 100})
for i in d:
    print(i)

d = collection.find({"qty": {"$gte": 100}})
for i in d:
    print(i)
"""
#d = collection.find({"item":"sketch pad" ,"qty":95})
#d=collection.find({"item":"sketch pad","qty":{"$gte":75}}) # and condition
"""
d=collection.find({"$or":[{"item":"sketch pad"},{"qty":{"$gte":75}}]})
for i in d:
    print(i)
"""
collection.update_one({"item": "canvas"},{"$set":{"item": "ABHILASH"}})
#d=collection.find()\
"""
d=collection.find({"item": "ABHILASH"})
for i in d:
    print(i)
"""
collection.delete_one({"item": "ABHILASH"})
d=collection.find()
for i in d :
    print(i)
