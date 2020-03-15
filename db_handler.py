import logging
import urllib.parse
from pymongo import MongoClient
from os import getenv

class MongoDriver():
    """Handles database methods"""
    DB_URI_STRING = ""
    USERNAME = ""
    PASSWORD = ""

    def __init__(self):
        self.USERNAME = urllib.parse.quote_plus('gb9864')
        self.PASSWORD = urllib.parse.quote_plus('05KMT7AcHMbVFMuP')
        self.DB_URI_STRING = str("mongodb+srv://" + self.USERNAME + ":" + self.PASSWORD + "@cluster0-yww2t.mongodb.net/tweets?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")


    def get_db_new_instance(self,db_name):
        db_client = MongoClient(self.DB_URI_STRING)
        db_test_db = db_client[str(db_name)]
        return db_test_db

if __name__ == '__main__':
    main()
