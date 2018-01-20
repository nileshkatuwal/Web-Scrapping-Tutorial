from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://techprotricks.com').text
soup = BeautifulSoup(source, 'html.parser')

csv_file = open('techprotricks.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','Category','Published Date','Summary'])

for article in soup.find_all('article'):

   headline = article.h2.a.text
   print(headline)
   cat = article.find('div', class_='above-entry-meta').a.text
   print(cat)
   pubtime = article.find('div', class_='below-entry-meta').time.text
   print(pubtime)
   summary = article.find('div', class_='entry-content clearfix').p.text
   print(summary)
   csv_writer.writerow([headline, cat, pubtime, summary ])
csv_file.close()
