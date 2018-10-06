from twython import Twython
import json

# keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 
credentials['CONSUMER_SECRET'] =
credentials['ACCESS_TOEKN'] =
credentials['ACCESS_SECRET'] =

#Save credentials object to file
With open("twitter_credentials.json", "w") as file:
	json.dump(credentials, file)

data = []
with open('dnac_devices.json', 'w') as file
	
	for line in file:
		data.append(json.loads(line)

for 
