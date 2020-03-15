# -*- coding: utf-8 -*-
import urllib.parse

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'TweetScraper'
TELNETCONSOLE_PORT = None

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO
CLOSESPIDER_TIMEOUT = 5

# To handle download delays
DOWNLOAD_DELAY = .25
RANDOMIZE_DOWNLOAD_DELAY = True

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToMongoPipeline':1000, # Save the data using Pipeline MongoDB Atlas cluster
}

# settings for mongodb
USERNAME = urllib.parse.quote_plus('gb9864')
PASSWORD = urllib.parse.quote_plus('05KMT7AcHMbVFMuP')
DB_URI_STRING = str("mongodb+srv://" + USERNAME + ":" + PASSWORD + "@cluster0-yww2t.mongodb.net/tweets?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")

MONGO_URI = DB_URI_STRING
MONGODB_DB = "tweets"  # database name to save the crawled tweets. Can also be changed in run time
MONGO_PIPE_TIMEOUT = 100000