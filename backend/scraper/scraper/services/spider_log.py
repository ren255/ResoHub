from time import time
import scrapy


class SpiderProcessLogger:
    """Spider処理のログ・統計管理クラス"""

    def __init__(self, spider: scrapy.Spider):
        self.spider = spider
        self.name = spider.name
        self.start_time = None
        self.count = 0

    def start(self):
        """処理開始"""
        self.start_time = time()
        self.count = 0
        print(f"{self.name} started")

    def processed(self, count: int = 1):
        """処理数を記録"""
        self.count += count

    def log(self):
        """進捗ログ出力"""
        elapsed = time() - self.start_time
        speed = self.count / elapsed if elapsed > 0 else 0
        print(f"{self.name}: {self.count} items, {speed:.2f} items/s, {elapsed:.2f}s")

    def complete(self):
        """処理完了・最終統計出力"""
        elapsed = time() - self.start_time
        speed = self.count / elapsed if elapsed > 0 else 0
        print(
            f"{self.name} completed: {self.count} items in {elapsed:.2f}s ({speed:.2f} items/s)"
        )
