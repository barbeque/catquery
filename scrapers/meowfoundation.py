from scraper import Scraper, CatListing
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
        result = []
        for name, image, link in zip(names, images, links):
            result.append(CatListing(name.text, image.get('src'), 'http://www.meowfoundation.com' + link.get('href')))
        return result
