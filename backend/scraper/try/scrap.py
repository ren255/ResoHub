# %%
import scrapy
from scrapy.crawler import CrawlerProcess


class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    allowed_domains = ["google.com"]
    start_urls = ["https://www.google.com"]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 2,
    }

    def parse(self, response):
        """メインページの解析"""
        self.logger.info(f'ページタイトル: {response.css("title::text").get()}')

        # ページの基本情報を抽出
        yield {
            "url": response.url,
            "title": response.css("title::text").get(),
            "status": response.status,
        }

        # リンクを抽出（最大5件）
        links = response.css("a::attr(href)").getall()[:5]
        for link in links:
            if link and link.startswith("http"):
                self.logger.info(f"リンク発見: {link}")
                yield {"link": link}


def main():
    """Scrapyクローラーを実行"""
    process = CrawlerProcess(
        {
            "LOG_LEVEL": "INFO",
            "FEEDS": {
                "output.json": {
                    "format": "json",
                    "encoding": "utf8",
                    "overwrite": True,
                },
            },
        }
    )

    process.crawl(GoogleSpider)
    process.start()


if __name__ == "__main__":
    main()
