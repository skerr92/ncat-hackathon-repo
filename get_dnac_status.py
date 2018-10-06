from twython import Twython
import json
import datetime

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
dataTime = datetime.datetime.now()
error_count = 0
down_devices = 0
newOutput= dataTime

with open('data.json', 'w') as file:
	
	for line in file:
		data.append(json.loads(line)


for item in data['response']
	
	if item['errorCode']==[null] & item['upTime']!=["0days 00:00:00.00"]
		
	
	else if item[errorCode']!=[null] & item['upTime']!=["0days 00:00:00.00"]
		error_count += 1
		
	else
		error_count += 1
		down_devices += 1
	if error_count==0
		print(dataTime + ": The Network is up! No issues detected")
	else if error_count>=1 && down_devices<4
		print(dataTime + ": The Network is up! (" + error_count + ") issues detected")
	else if error_count>=1 && down_devices==4
		print(dataTime + ": ALERT! The Network is down! (" + error_count + ") issues detected")
#print(new_output)


