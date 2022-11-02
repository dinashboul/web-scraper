import os
import requests
from bs4 import BeautifulSoup
import json
URL='https://en.wikipedia.org/wiki/History_of_Mexico'

page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

def get_citations_needed_count(url):
  '''
  >>> get_citations_needed_count function is to calculate the count of citation needed 
  '''
  count = 0
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  citations = soup.find_all('a',title="Wikipedia:Citation needed")
  for word in citations:
    if word.text == 'citation needed':
      count+=1
      
  return count


def get_citations_needed_report(url):
  '''
    >>> get_citations_needed_report function is return formatted with each citation listed in the order found 
  ''' 
  passages = ""
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.find_all('p')

  for title in titles:
    if 'citation needed' in title.text.strip():
      passages+=title.text.strip()

    with open('posts.json','w') as file:
        for report in passages:
            file.write(report)
         



if __name__=="__main__":

    print("the number of citation neede is --->",get_citations_needed_count(URL))
    get_citations_needed_report(URL)