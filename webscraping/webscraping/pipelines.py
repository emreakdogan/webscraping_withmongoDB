import pymongo
import os
class MongoDBPipeline:
    def __init__(self, connection_string, database):
        self.connection_string = connection_string
        self.checkpoint_file = 'check.txt' # control 
        self.database = database
        

    @classmethod
    def from_crawler(cls, crawler):
        connection_string = crawler.settings.get('MONGODB_CONNECTION_STRING')
        database = crawler.settings.get('MONGODB_DATABASE')
        return cls(connection_string, database)

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[self.database]
        
        if os.path.exists(self.checkpoint_file): 
            with open(self.checkpoint_file, 'r') as file:
                last_url = file.read().strip()  # last  html
                self.start_urls = [last_url]   # set last html to start_urls

    def close_spider(self, spider):
        self.client.close()
        with open(self.checkpoint_file, 'w') as file: # write last html
            file.write(spider.start_urls[0])

    def process_item(self, item, spider):
        collection_name = 'kitapyurdu' if spider.name == 'kitapyurdu' else 'kitapsepeti'
        self.db[collection_name].insert_one(item)
        return item

