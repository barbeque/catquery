from scraper import Scraper
import requests
from lxml import etree
from pyquery import PyQuery as pq

class MeowFoundationScraper(Scraper):
    def __init__(self):
        self.url = 'http://www.meowfoundation.com/adopt/'
    def scrape(self):
        namesQuery = '#maincats > div > h2'
        linksQuery = '#maincats > div > .forward'
        imgQuery = '#maincats > div > a > .cat-thumb > img'
        r = requests.get(self.url)
        content = r.text

        querier = pq(content)

        names = querier(namesQuery)
        links = querier(linksQuery)
        images = querier(imgQuery)

        # TODO: parse the extracted html
        for name, image, link in zip(names, images, links):
            print '==Cat=='
            print name
            print image
            print link

        return []
