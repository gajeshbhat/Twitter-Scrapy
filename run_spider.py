import scrapy
import json
import threading
import time
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
		{'city_name':'tehran','country_name':'Iran'},
		{'city_name':'Berlin','country_name':'Germany'},
		{'city_name':'Rome','country_name':'Italy'},
		{'city_name':'London','country_name':'England'},
		{'city_name':'New York','country_name':'United States'},
		{'city_name':'Paris','country_name':'France'},
		{'city_name':'Tokyo','country_name':'Japan'},
		{'city_name':'Moscow','country_name':'Russia'},
		{'city_name':'Barcelona','country_name':'Spain'},
		{'city_name':'Madrid','country_name':'Spain'},
		{'city_name':'Amsterdam','country_name':'Netherlands'},
		{'city_name':'Beijing','country_name':'China'},
		{'city_name':'Toronto','country_name':'Canada'},
		{'city_name':'Doha','country_name':'Qatar'},
		{'city_name':'Sydney','country_name':'Australia'},
		{'city_name':'Vancouver','country_name':'Canada'},
		{'city_name':'Lisbon','country_name':'Portugal'},
		{'city_name':'Budapest','country_name':'Hungary'},
		{'city_name':'Istanbul','country_name':'Turkey'},
		{'city_name':'Vienna','country_name':'Austria'},
		{'city_name':'Seoul','country_name':'South Korea'},
		{'city_name':'Bangkok','country_name':'Thailand'},
		{'city_name':'Dublin','country_name':'Ireland'},
		{'city_name':'Bengaluru','country_name':'India'},
		{'city_name':'New Delhi','country_name':'India'},
		{'city_name':'Jaipur','country_name':'India'},
		{'city_name':'Athens','country_name':'Greece'}
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

def hard_refresh(city_country_dict):
	db_obj = MongoDriver()
	db_inst = db_obj.get_db_new_instance('tweets')
	for entry in city_country_dict:
		db_country_collection = db_inst[entry['country_name']]
		db_country_collection.delete_many({})

def crawl_top_cities():
	top_cities = get_top_cities()
	crawler_settings = get_project_settings()
	craw_process = CrawlerProcess(crawler_settings)
	for city in top_cities:
		craw_process.crawl(TweetScraper, query=str(city['city_name']),country=city['country_name'],lang='en',top_tweet=True)
	craw_process.start() # Better to run this in a thread and not to interfer with Flask process

def run_timed_crawl(time_in_seconds):
	# Crawl all cities
	while True:
		city_list = get_top_cities()
		hard_refresh(city_list)
		crawl_top_cities()
		time.sleep(time_in_seconds)

# Run crawler for every n seconds
run_timed_crawl(300)

		