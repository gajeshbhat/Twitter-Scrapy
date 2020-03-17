from flask import Flask
from flask_restful import Resource, Api
from fetch import get_city_info, get_single_country
from json import dumps

app = Flask(__name__)
api = Api(app)

class RawTweets(Resource):
    def get(self,country_name,city_name=''):
    	if city_name == '':
    		return get_single_country(country_name)
    	return  get_city_info(city_name,country_name)

    def put(self,country_name,city_name=''):
        return {'status' : 'ok','message' : 'hello world'}

api.add_resource(RawTweets, '/raw_tweets/<string:country_name>/',
							'/raw_tweets/<string:country_name>/<string:city_name>')

if __name__ == '__main__':
    app.run(debug=True)