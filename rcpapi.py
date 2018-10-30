import sys
import requests, json
import pandas as pd
token_url ='http://rcp.nctu.me:8000/api/token/'
get_class_url = 'http://rcp.nctu.me:8000/api/curriculum/subjects/'
token_json = {'username': 'admin', 'password':'123@Admin'}
token_header = {'Content-Type': 'application/json'}

post_token  =  requests.post(url=token_url,json= token_json, headers = token_header)
token = post_token.json()
refresh_token = token ['refresh']
access_token = token['access']

class_header = {'Authorization':'Bearer '+access_token}

get_class = requests.get(url = get_class_url, headers = class_header)
class_json = get_class.json()

for start_times in class_json:
    start_times = class_json[0]['section_times'][0]['start_time']

print(class_json[0]['section_times'][0]['start_time'])
print(start_times)
# print(class_start_time)