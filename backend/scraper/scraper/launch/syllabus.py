import scraper.settings
from scrapy.utils.log import configure_logging

configure_logging()

from twisted.internet import defer
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
from ..spiders import (
    CollegesOverviewSpider,
    DepartmentsOverviewSpider,
    DepartmentDetailSpider,
    SubjectCatalogSpider,
    SubjectDetailSpider,
)
from shortuuid import uuid


@defer.inlineCallbacks
def crawl():
    scrape_id = uuid()[-8:]
    runner = CrawlerRunner(get_project_settings())
    yield runner.crawl(CollegesOverviewSpider, uuid=scrape_id, school_id="14")
    yield runner.crawl(DepartmentsOverviewSpider, uuid=scrape_id)
    yield runner.crawl(DepartmentDetailSpider, uuid=scrape_id)
    yield runner.crawl(SubjectCatalogSpider, uuid=scrape_id)
    yield runner.crawl(SubjectDetailSpider, uuid=scrape_id)
    from twisted.internet import reactor

    reactor.stop()


def parallel():
    scrape_id = uuid()[-8:]
    process = CrawlerProcess(get_project_settings())
    process.crawl(CollegesOverviewSpider, uuid=scrape_id)
    process.crawl(DepartmentsOverviewSpider, uuid=scrape_id)
    process.crawl(SubjectCatalogSpider, uuid=scrape_id, school_id="14")
    process.start()


if __name__ == "__main__":
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

    crawl()
    from twisted.internet import reactor

    reactor.run()
