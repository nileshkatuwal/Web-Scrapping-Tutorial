from bs4 import BeautifulSoup
import requests

source = requests.get('http://techprotricks.com').text
soup = BeautifulSoup(source, 'html.parser')
#print(soup.prettify())
t = soup.title.text
print(t)
