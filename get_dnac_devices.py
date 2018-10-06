#! /usr/bin/env python3

from env_lab import dnac
import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable



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
    dnac_dict = dict()
    dnac_dict['hostname']==[]
    dnac_dict['platformId']==[]
    dnac_dict['softwareType']==[]
    dnac_dict['softwareVersion']==[]
    dnac_dict['upTime']==[]
    for item in data['response']:
        dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"]])
    for key in dnac_dict:
	if dnac_dict[key]==dnac_devices.get(item):
		dnace_dict[key].append(dnac_devices)
	

login = dnac_login(dnac["host"], dnac["username"], dnac["password"])
network_device_list(dnac, login)

print(dnac_devices)

with open('dnac_dict.json', 'w') as outfile:
	json.dump(dnac_dict, outfile)
