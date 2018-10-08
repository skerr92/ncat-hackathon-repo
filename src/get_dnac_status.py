#! /usr/bin/env python3

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
	dnac_devices = PrettyTable(['Hostname','Platform Id','Software Type','Software Version','Up Time' ])
	dnac_devices.padding_width = 1

	# Silence the insecure warning due to SSL Certificate
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

	headers = {
              	'content-type': "application/json",
              'x-auth-token': ""
        }


	def dnac_login(host, username, password):
    	    url = "https://{}/api/system/v1/auth/token".format(host)
    	    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                headers=headers, verify=False)
    	    return response.json()["Token"]


	def network_device_list(dnac, token):
    	    url = "https://{}/api/v1/network-device".format(dnac['host'])
    	    headers["x-auth-token"] = token
            response = requests.get(url, headers=headers, verify=False)
    	    data = response.json()
    	    with open('data.json', 'w') as outfile:
	        json.dump(data, outfile)
    	    for item in data['response']:
        	dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"]])

		
	

	    login = dnac_login(dnac["host"], dnac["username"], dnac["password"])
	    network_device_list(dnac, login)

	    print(dnac_devices)	

	Tweetdata = []
	ts=time.time()
	dataTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	index = 1
	error_count = 0
	down_devices = 0


	Tweetdata = json.loads(open ('data.json').read())
	#Tweetdata = json.load('{"errorCode":,"upTime":}')


	for item in Tweetdata['response']:
	#for item in data['response'][index]:
	
		if (item["errorCode"]==None) & (item["upTime"]!="0 days, 00:00:00.00"):
			error_count = error_count
			down_devices = down_devices
	
		elif (item["errorCode"]!=None) & (item["upTime"]!="0 days, 00:00:00.00"):
			error_count += 1
			down_devices = down_devices
		
		else:
			error_count += 1
			down_devices += 1

	if error_count==0:
		twitter.update_status(status=dataTime + ": The Network is up! No issues detected")
	elif error_count>=1 & down_devices<4:
		twitter.update_status(status=dataTime + ": The Network is up! (" + str(error_count) + ") issues detected")
	elif error_count>=1 & down_devices==4:
		twitter.update_status(status=dataTime + ": ALERT! The Network is down! (" + str(error_count) + ") issues detected")

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=1)
scheduler.start()


