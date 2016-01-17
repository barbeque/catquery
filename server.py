from scraper import Scraper
from scrapers.meowfoundation import *
from scrapers.aarcs import *
from operator import attrgetter
from jinja2 import Environment, FileSystemLoader

scrapers = [ MeowFoundationScraper(), AarcsScraper() ]
cats = []

env = Environment(loader=FileSystemLoader('templates'))

for scraper in scrapers:
    cats = cats + scraper.scrape()

cats.sort(key = attrgetter('name'))

template = env.get_template('catlisting.html')
with open('cats.html', 'w') as f:
    f.write(template.render(cats = cats))
