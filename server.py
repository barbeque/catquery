from scraper import Scraper
from scrapers.meowfoundation import *
from operator import attrgetter

scrapers = [ MeowFoundationScraper() ]
cats = []

for scraper in scrapers:
    cats = cats + scraper.scrape()

cats.sort(key = attrgetter('name'))

for cat in cats:
    print cat.name, cat.link
