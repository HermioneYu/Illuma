import requests
import json

import sys

file_name = sys.argv[1]

file_dir = sys.argv[2]
#print(file_dir)

url = "http://api.meaningcloud.com/lang-2.0"

key = 'ef5ef5d34e8666e1f03a9269256ec52b'
payload = {'key':key,'doc':file_name}
files = {'doc':open(file_dir,'rb')}
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, files=files)


data = json.loads(response.text)


language_list = data['language_list']

language_type = language_list[0]['name']

print('The file ' + file_name +' is in language: '+ language_type)
