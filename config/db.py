from pymongo import MongoClient


# connectionString = "mongodb://localhost:27017"
connectionString = "mongodb+srv://supratim531:sayan2002%40@cluster0.okgdt49.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(connectionString)
db = client.test


if __name__ == "__main__":
    print(client, db)
    pass
