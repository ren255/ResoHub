import scraper.settings
from scrapy.utils.log import configure_logging

configure_logging()

from twisted.internet import defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
from scraper.spiders import (
    CollegesOverviewSpider,
    DepartmentsOverviewSpider,
    DepartmentDetailSpider,
    SubjectCatalogSpider,
    SubjectDetailSpider,
)
from shortuuid import uuid
import subprocess
import sys


@defer.inlineCallbacks
def crawl(scrape_id):
    runner = CrawlerRunner(get_project_settings())
    yield runner.crawl(CollegesOverviewSpider, uuid=scrape_id, school_id="14")
    yield runner.crawl(DepartmentsOverviewSpider, uuid=scrape_id)
    yield runner.crawl(DepartmentDetailSpider, uuid=scrape_id)
    yield runner.crawl(SubjectCatalogSpider, uuid=scrape_id)
    yield runner.crawl(SubjectDetailSpider, uuid=scrape_id)
    from twisted.internet import reactor

    reactor.stop()


if __name__ == "__main__":
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

    scrape_id = uuid()[-8:]
    crawl(scrape_id)
    from twisted.internet import reactor

    reactor.run()

    try:
        result = subprocess.run(
            [sys.executable, "-m", "data_export.exporter", "--scrape-id", scrape_id],
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
        print(f"Data export completed successfully for scrape ID: {scrape_id}")
    except subprocess.CalledProcessError as e:
        print(f"Error during data export: {e}")
        print(e.stderr)
