import scrapy
import bet365_it.Bet365 as bet_it
from argparse import Namespace
from scrapy.utils.project import get_project_settings
SETTINGS = get_project_settings()

class Bet365Spider(scrapy.Spider):
    name = "Bet365_it"
    def start_requests(self):
        options = Namespace(allstart=False, bookie='Bet365', cycle=None, database=SETTINGS['DB_NAME'], host=SETTINGS['DB_HOST'], noproxies=SETTINGS['NOPROXY_FLAG'], password=SETTINGS['DB_PASS'], residentials=SETTINGS['RESIDENTIALS_FLAG'], sport='CALCIO', threads=16, username='prodev', usetor=False)
        bot = bet_it.Bet365(options)
        bot.run()
