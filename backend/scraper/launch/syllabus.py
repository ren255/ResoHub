import argparse
import scraper.settings
from scrapy.utils.log import configure_logging

configure_logging()
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
from data_export import Exporter
from shortuuid import uuid
from twisted.internet import defer


@defer.inlineCallbacks
def crawl(scrape_id):
    """Twisted の inlineCallbacks でクローラーを順次実行"""
    runner = CrawlerRunner(get_project_settings())

    # 各スパイダーを順次実行
    yield runner.crawl(CollegesOverviewSpider, uuid=scrape_id, school_id="14")
    yield runner.crawl(DepartmentsOverviewSpider, uuid=scrape_id)
    yield runner.crawl(DepartmentDetailSpider, uuid=scrape_id)
    yield runner.crawl(SubjectCatalogSpider, uuid=scrape_id)
    yield runner.crawl(SubjectDetailSpider, uuid=scrape_id)

    print(f"Crawling completed: {scrape_id}")

    # クローリング完了後にデータエクスポート
    yield defer.ensureDeferred(Exporter(scrape_id).run())

    print(f"Export completed: {scrape_id}")

    from twisted.internet import reactor

    reactor.stop()


@defer.inlineCallbacks
def export_only(scrape_id):
    """エクスポートのみを実行"""
    print(f"Starting export for ID: {scrape_id}")

    yield defer.ensureDeferred(Exporter(scrape_id).run())

    print(f"Export completed: {scrape_id}")

    from twisted.internet import reactor

    reactor.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Syllabus scraper and exporter")
    parser.add_argument(
        "--export", type=str, help="Export only for the specified scrape ID"
    )

    args = parser.parse_args()

    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")

    if args.export:
        # エクスポートのみ実行
        print(f"Export mode: {args.export}")
        export_only(args.export)
    else:
        # 通常のクローリング＋エクスポート
        scrape_id = uuid()[-8:]
        print(f"Starting crawl with ID: {scrape_id}")
        crawl(scrape_id)

    from twisted.internet import reactor

    reactor.run()
