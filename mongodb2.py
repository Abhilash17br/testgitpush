import pymongo

client = pymongo.MongoClient("mongodb+srv://root:fsds2022@abhilash.mdw9l.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client["myinfo"]
collection=database['abhi']

"""
data=collection.find({"companyName":"iNeuron"})
for i in data:
    print(i)

data= collection.find({"courseOffered":{"$gt":"E"}})
for i in data:
    print(i)
"""
