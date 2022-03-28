from bs4 import BeautifulSoup
import requests


site = requests.get('https://weather.com/weather/today/l/74fa88d47faeefd5c81862986b5c7fb6266cab3fa17be359ef7ebd219ae222f2').content


soup = BeautifulSoup(site, 'html.parser')

temp = soup.find('span', class_="CurrentConditions--tempValue--3a50n")

print(soup.prettify())
print(temp.string)
print(soup.p.string)
