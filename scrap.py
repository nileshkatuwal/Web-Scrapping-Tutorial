from bs4 import BeautifulSoup
import requests

source = requests.get('http://techprotricks.com').text
soup = BeautifulSoup(source, 'html.parser')
#print(soup.prettify())
#t = soup.title.text
#print(t)
headline = article.h2.a.text
cat = article.find('div', class_ = 'above-entry-meta').a.text
pubtime = article.find('div', class_ = 'below-entry-meta').time.text
summary = article.find('div', class_ = 'entry-content clearfix').p.text
print(headline)
print(cat)
print(pubtime)
print(summary)
