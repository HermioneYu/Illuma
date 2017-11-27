import requests
import json
from pprint import pprint


url = "http://api.meaningcloud.com/lang-2.0"

key = 'ef5ef5d34e8666e1f03a9269256ec52b'
payload = {'key':key,'doc':'chinese.docx'}
files = {'doc':open('/Users/Hermione/Illuma/data/chinese.docx','rb')}
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, files=files)

#print(response.text)


data = json.loads(response.text)

#pprint(data)

language_list = data['language_list']

language_type = language_list[0]['name']

print('The file is in language: '+ language_type)


