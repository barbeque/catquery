from scraper import Scraper, CatListing
import requests
from lxml import etree
from pyquery import PyQuery as pq

class AarcsScraper(Scraper):
    def __init__(self):
        self.url = 'http://aarcs.ca/adoptable-cats/'
    def scrape(self):
        namesQuery = '.entry-content > h3'
        linksQuery = '.inner-entry > a'
        imgQuery = '.inner-entry > a > img'
        r = requests.get(self.url)
        content = r.text

        querier = pq(content)

        names = querier(namesQuery)
        links = querier(linksQuery)
        images = querier(imgQuery)

        # TODO: parse the extracted html
        result = []
        for name, image, link in zip(names, images, links):
            result.append(CatListing(name.text.encode('ascii', 'ignore').strip(), image.get('src'), link.get('href')))
        return result
