import requests
import random
import os

if not os.path.exists('result'):
    os.makedirs('result')

with open('ua/randua.txt', 'r') as f:
    ua_list = f.readlines()

ua_list = [ua.strip() for ua in ua_list]

ua = random.choice(ua_list)

headers = {'User-Agent': ua}

url = 'https://www.facebook.com/'
response = requests.get(url, headers=headers)

cookie = response.cookies.get_dict()
token = cookie['access_token']

filename = 'result/token.txt'
with open(filename, 'w') as f:
    f.write(token)

print("User-Agent: ", headers['User-Agent'])
print("Token disimpan di: ", filename)
