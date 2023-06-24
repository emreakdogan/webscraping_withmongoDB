import scrapy
import pymongo
from bson import json_util
import json
from scrapy import cmdline
class BookStoreSpider(scrapy.Spider):
    name = 'kitapyurdu'
    allowed_domains = ['www.kitapyurdu.com']
    start_urls = ['https://www.kitapyurdu.com/kategori/kitap-egitim-dil-egitimi/1_359_364.html']
    #location of csv file and encoding utf-8
    custom_settings = {
    'FEED_EXPORT_ENCODING': 'utf-8',
    'MONGODB_CONNECTION_STRING': 'mongodb://localhost:27017',
    'MONGODB_DATABASE': 'smartmaple',
    'MONGODB_COLLECTIONS': ['kitapyurdu', 'kitapsepeti']
}
    
# response.css(".name.ellipsis a::attr(title)").extract() -> Title
# response.css(".author .alt span::text ").extract() -> Author
# response.css(".publisher .alt span::text ").extract() -> Publisher
# response.css(".price .price-new .value::text ").extract() -> Price

    def parse(self, response):
           #Extract product information
       titles = response.css(".name.ellipsis a::attr(title)").extract()
       authors = response.css(".author .alt span::text ").extract()
       publishers = response.css(".publisher .alt span::text ").extract()
       prices = response.css(".price .price-new .value::text ").extract()
       for item in zip(titles,authors,publishers,prices):
            book = {
            'title' : item[0],
            'writers' : item[1],
            'publisher' : item[2], 
            'price' : item[3]
           }
            
            yield  json.loads(json_util.dumps(book))
            
       next_page = response.css('.pagination .links .next::attr(href)').get()
       if next_page is not None:
        self.start_urls[0] = next_page # control 
        yield response.follow(next_page, callback=self.parse)












