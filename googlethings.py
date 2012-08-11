import sys
import urllib2
from bs4 import BeautifulSoup

def google(search_query):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    search_query = '+'.join(search_query.split()) # replaces spaces in query with '+' for URL
    search_url = 'https://www.google.com/search?q=' + search_query
    print search_url
    page = opener.open(search_url)
    # print page
    data = page.read()
    soup = BeautifulSoup(data)
    # print soup.prettify()
    result = soup.find_all(id='search')
    url_result = str(result[0].a)
    start = url_result.find('?q=') # url follows
    start = start + 3 #adjust for length of searched string
    end = url_result.find('&amp')
    url = url_result[start:end]
    return url


if __name__ == '__main__':
    search = raw_input("Enter your query:")
    link = google(search)
