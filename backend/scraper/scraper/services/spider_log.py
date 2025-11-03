from time import time
import scrapy


class SpiderProcessLogger:
    """Spider処理のログ・統計管理クラス"""

    def __init__(self, spider: scrapy.Spider):
        self.spider = spider
        self.logger = spider.logger  # Scrapyのlogger
        self.name = spider.name
        self.start_time = None
        self.count = 0

    def start(self):
        """処理開始"""
        self.start_time = time()
        self.count = 0
        self.logger.info(f"{self.name} started")

    def processed(self, count: int = 1):
        """処理数を記録"""
        self.count += count

    def log(self):
        """進捗ログ出力"""
        elapsed = time() - self.start_time
        speed = self.count / elapsed if elapsed > 0 else 0
        self.logger.info(
            f"{self.name}: {self.count} items, {speed:.2f} items/s, {elapsed:.2f}s"
        )

    def complete(self):
        """処理完了・最終統計出力"""
        elapsed = time() - self.start_time
        speed = self.count / elapsed if elapsed > 0 else 0
        self.logger.info(
            f"{self.name} completed: {self.count} items in {elapsed:.2f}s ({speed:.2f} items/s)"
        )


# 使用例（Spiderクラス内での利用）
"""
class ExampleSpider(scrapy.Spider):
    name = "example"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.process_logger = SpiderProcessLogger(self)
    
    async def start_requests(self):
        self.process_logger.start()
        # ... requests
    
    def parse(self, response):
        # ... parsing
        self.process_logger.processed(1)
        
        if self.process_logger.count % 25 == 0:
            self.process_logger.log()
    
    async def spider_closed(self, spider):
        self.process_logger.complete()
"""
