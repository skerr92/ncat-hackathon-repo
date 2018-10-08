from twython import Twython
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import time
from env_lab import dnac
import json
import requests
import urllib3
import logging
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

logging.basicConfig()

twitter_mentions = PrettyTable(['id_str'])
twitter_mentions.padding_width = 1

# keys/secrets as strings in the following fields
credentials = {}
APP_KEY = ""
APP_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# Instantiate an object
twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
twitter.verify_credentials()
twitter.get_home_timeline()

def some_job():
    Tweetdata = []
    ts=time.time()
    dataTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    mention_result = twitter.cursor(twitter.get_mentions_timeline)
    for result in mention_result:
	twitter_mentions.add_row(result['id_str'])
print(twitter_mentions)