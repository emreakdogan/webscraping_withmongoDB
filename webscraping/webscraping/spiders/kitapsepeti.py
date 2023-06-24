import scrapy
import pymongo
from bson import json_util
import json
from scrapy import cmdline
class BookStoreSpider(scrapy.Spider):
    name = 'kitapsepeti'
    allowed_domains = ['www.kitapsepeti.com']
    start_urls = ['https://www.kitapsepeti.com/roman']
    #location of csv file and encoding utf-8
    custom_settings = {
    'FEED_EXPORT_ENCODING': 'utf-8',
    'MONGODB_CONNECTION_STRING': 'mongodb://localhost:27017',
    'MONGODB_DATABASE': 'smartmaple',
    'MONGODB_COLLECTIONS': ['kitapyurdu', 'kitapsepeti']
}

    # parse process
    def parse(self, response):
           #Extract product information
       titles = response.css(".row .fl.col-12.text-description.detailLink::text").extract()
       authors = response.css(".row .fl.col-12.text-title::text").extract()
       publishers = response.css(".row .col.col-12.text-title.mt::text").extract()
       prices = response.css(".box.col-10.col-ml-1.col-sm-12.proRowAct .col.col-12.currentPrice::text").extract()
       for item in zip(titles,authors,publishers,prices):
            book = {
            'title' : item[0].strip().replace('\n', ''),
            'author' : item[1],
            'publisher' : item[2], 
            'price' : item[3].strip().replace('\n', '')
           }
            yield  json.loads(json_util.dumps(book))
            
       next_page = response.css('.row  .next::attr(href)').get()
       if next_page is not None:
        self.start_urls[0] = next_page # control 
        yield response.follow(next_page, callback=self.parse)





