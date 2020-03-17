import scrapy
import json
import threading
from scrapy.crawler import CrawlerProcess
from TweetScraper.spiders.TweetCrawler import TweetScraper
from scrapy.utils.project import get_project_settings
from db_handler import MongoDriver
from pprint import pprint

# To be done for loading from the database.
def load_top_cities():
	return None

# To be implemeted to fetch from database
def get_top_cities():
	return list([
		{'city_name':'manchaster','country_name':'UK'},
		{'city_name':'mumbai','country_name':'India'},
		{'city_name':'bejing','country_name':'China'},
		{'city_name':'tehran','country_name':'Iran'},
		])

def get_single_country(country_name):
	db_obj = MongoDriver()
	db_inst = db_obj.get_db_new_instance('tweets')
	db_inst_collection = db_inst[country_name]
	country_data = db_inst[str(country_name)].find({})

	if city_data:
		pprintprint(city_data)
		return dict({'status':'success','tweet_details':list(city_data)})
	return list({'status':'error!','tweet_details':[]})

def get_city_info(city_name,country_name):
	db_obj = MongoDriver()
	db_inst = db_obj.get_db_new_instance('tweets')
	db_inst_collection = db_inst[country_name]
	city_data = db_inst[str(country_name)].find({'hash_tag':str(city_name)})

	if city_data:
		return {'status':'success','tweet_details':list(city_data)}
	return list({'status':'error!','tweet_details':[]})

def crawl_single_city(city_name,country_name,is_single_crawl=True):
	crawler_settings = get_project_settings()
	craw_process = CrawlerProcess(crawler_settings)
	craw_process.crawl(TweetScraper, query=str(city_name),country=country_name,lang='en',top_tweet=True)
	craw_process.start() # Script blocks here until crawl is done
	if is_single_crawl is True:
		return get_city_info(city_name,country_name)

def crawl_top_cities():
	top_cities = get_top_cities()
	crawler_settings = get_project_settings()
	craw_process = CrawlerProcess(crawler_settings)
	for city in top_cities:
		craw_process.crawl(TweetScraper, query=str(city['city_name']),country=city['country_name'],lang='en',top_tweet=True)
	craw_process.start() # Better to run this in a thread and not to interfer with Flask process

# test code
crawl_top_cities()