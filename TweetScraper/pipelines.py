# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import logging
import pymongo
import json
import os

from TweetScraper.items import Tweet

SETTINGS = get_project_settings()

logger = logging.getLogger(__name__)

class SaveToMongoPipeline(object):

    ''' Pipeline to save tweets to mongodb with each country as collection name'''
    connection = None
    db =  None

    def __init__(self):
        self.connection = pymongo.MongoClient(SETTINGS['MONGO_URI'],connectTimeoutMS=SETTINGS['MONGO_PIPE_TIMEOUT'])
        self.db = self.connection[SETTINGS['MONGODB_DB']]

    def process_item(self, item, spider):
        
        self.tweetCollection = self.db[item['city_country']]
        self.tweetCollection.ensure_index([('ID', pymongo.ASCENDING)], unique=True, dropDups=True)

        tweet_exist_check = self.tweetCollection.find_one({'ID':item['ID']})
        if tweet_exist_check:
            pass # If tweets already exist, dont insert.
        else:
            self.tweetCollection.insert_one( dict(item) )
            logger.debug("Add tweet:%s" %item['url'])
