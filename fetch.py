from db_handler import MongoDriver
from pprint import pprint
from bson.json_util import dumps

def get_single_country(country_name):
	db_obj = MongoDriver()
	db_inst = db_obj.get_db_new_instance('tweets')
	db_inst_collection = db_inst[country_name]
	country_data = db_inst[str(country_name)].find({})

	if country_data:
		return dict({'status':'success','tweet_details':dumps(list(country_data))})
	return list({'status':'error!','tweet_details':[]})

def get_city_info(city_name,country_name):
	db_obj = MongoDriver()
	db_inst = db_obj.get_db_new_instance('tweets')
	db_inst_collection = db_inst[country_name]
	city_data = db_inst[str(country_name)].find({'hash_tag':str(city_name)})

	if city_data:
		return {'status':'success','tweet_details':dumps(list(city_data))}
	return list({'status':'error!','tweet_details':[]})