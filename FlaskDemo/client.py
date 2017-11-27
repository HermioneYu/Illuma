import requests

#detect language of user input
user_info = {'name': 'letian', 'password': '123'}
text = input('Type anything:')
payload = {'txt':text}
r = requests.post("http://127.0.0.1:5000/text", data=payload)
print(r.text)

#detect language of a file
files = {'doc':open('/Users/Hermione/Illuma/data/chinese.docx','rb')}
payload = {'name':'chinese.docx'}
r = requests.post("http://127.0.0.1:5000/uploadfile", data=payload, files=files)




print(r.text)