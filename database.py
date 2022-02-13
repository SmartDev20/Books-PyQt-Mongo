import pymongo


class DataBase(object):
    def __init__(self, url, dbs):
        self.url = url
        self.dbs = dbs
        self.client = pymongo.MongoClient(url)
        self.db = self.client[dbs]

    def find_one(self, collection, query):
        return self.db[collection].find_one(query, {"_id": 0})

    def insert_one(self, collection, data):
        self.db[collection].insert_one(data)

    def delete(self, collection, query):
        self.db[collection].delete_one(query)

    def find_many(self, collection, query):
        return self.db[collection].find(query, {"_id": 0})

    def update(self, collection, query, new_value):
        self.db[collection].update_one(query, {'$set': new_value})
