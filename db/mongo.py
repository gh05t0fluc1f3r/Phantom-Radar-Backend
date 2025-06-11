from pymongo import MongoClient

class DBClient:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client.phantom_radar

    def insert_many(self, collection: str, data: list):
        self.db[collection].insert_many(data)

    def search(self, collection: str, keyword: str, severity: str = None):
        query = {"description": {"$regex": keyword, "$options": "i"}}
        if severity:
            query["cvss_severity"] = severity
        return list(self.db[collection].find(query, {"_id": 0}))

db_client = DBClient()
