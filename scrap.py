from bs4 import BeautifulSoup
import requests

source = requests.get('http://techprotricks.com').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

