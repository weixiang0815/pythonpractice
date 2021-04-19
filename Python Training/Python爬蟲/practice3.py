from bs4 import BeautifulSoup
import requests

data = requests.get('http://www.google.com').content
soup = BeautifulSoup(data, 'html.parser')
print(soup.body.div.attrs)
