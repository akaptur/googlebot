import sys
import pyrc
import pyrc.utils.hooks as hooks
import urllib2
from bs4 import BeautifulSoup

class googlerBot(pyrc.Bot):
    # @hooks.command()
    # def sayhi(self,channel):
    #     self.message(channel, "Hello!")

    @hooks.command(r'(.*)')
    def google(self,channel,search_query):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        search_query = '+'.join(search_query.split()) # replaces spaces in query with '+' for URL
        search_url = 'https://www.google.com/search?q=' + search_query
        page = opener.open(search_url)
        data = page.read()

        soup = BeautifulSoup(data)
        print soup.prettify()
        result = soup.find_all(id='search')
        if len(result) == 0:
            self.message(channel, 'Sorry, something went wrong.')
            return
        url_result = str(result[0].a)
        start = url_result.find('?q=') # url follows
        start = start + 3 #adjust for length of searched string
        end = url_result.find('&amp')
        url = url_result[start:end]
        
        self.message(channel, url)

if __name__ == '__main__':
    googbot = googlerBot('irc.freenode.net',channels = ['#test-google-bot'])
    googbot.connect()