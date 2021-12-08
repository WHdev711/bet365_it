import scrapy
import bet365_it.Bet365 as bet_it
# import bet365_token



class Bet365Spider(scrapy.Spider):
    name = "Bet365_it"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    # bet_it.Bet365()
    # bet_it.Bet365.get_leagues('football')
    def parse(self, response):

        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)