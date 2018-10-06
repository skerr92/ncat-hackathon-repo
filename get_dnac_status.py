from twython import Twython
import json
import datetime
import time

# keys/secrets as strings in the following fields
#credentials = {}
#credentials['CONSUMER_KEY'] = 
#credentials['CONSUMER_SECRET'] =
#credentials['ACCESS_TOEKN'] =
#credentials['ACCESS_SECRET'] =

#Save credentials object to file
#With open("twitter_credentials.json", "w") as file:
	#json.dump(credentials, file)

data = []
ts=time.time()
dataTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
index = 1
error_count = 0
down_devices = 0
print(dataTime)

data = json.loads(open ('data.json').read())
#data = json.load('{"errorCode":,"upTime":}')


for item in data['response']:
	#for item in data['response'][index]:
	
	if (item["errorCode"]=="null") & (item["upTime"]!="0days, 00:00:00.00"):
		error_count = error_count
		down_devices = down_devices
	
	elif (item["errorCode"]!="null") & (item["errorCode"]!="0days, 00:00:00.00"):
			error_count += 1
			down_devices = down_devices
		
	else:
		error_count += 1
		down_devices += 1

	if error_count==0:
		print(dataTime + ": The Network is up! No issues detected")
	elif error_count>=1 & down_devices<4:
		print(dataTime + ": The Network is up! (" + str(error_count) + ") issues detected")
	elif error_count>=1 & down_devices==4:
		print(dataTime + ": ALERT! The Network is down! (" + str(error_count) + ") issues detected")
#print(new_output)


