import scrapy
import bet365_it.Bet365 as bet_it
from argparse import Namespace
# import bet365_token



class Bet365Spider(scrapy.Spider):
    name = "Bet365_it"
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]
    # bet_it.Bet365.get_leagues('football')
    def start_requests(self):

        options = Namespace(allstart=False, bookie='Bet365', cycle=None, database='ninjabet_test', host='localhost', noproxies=False, password='', residentials=False, sport='CALCIO', threads=16, username='prodev', usetor=False)
        bot = bet_it.Bet365(options)
        bot.run()
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)