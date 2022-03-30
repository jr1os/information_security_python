import re
import json
from urllib.request import urlopen


url = 'http://ipinfo.io/json'

resp = urlopen(url)

data = json.load(resp)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']

print(data)
print(f"Ip: {ip} city: {city} country: {country}")
