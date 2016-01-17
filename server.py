from scraper import Scraper
from scrapers.meowfoundation import *

scrapers = [ MeowFoundationScraper() ]

for scraper in scrapers:
    scraper.scrape()
