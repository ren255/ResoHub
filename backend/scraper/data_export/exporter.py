import scraper.settings
from .loader import DataLoader
from .processors import Processor
import argparse
import asyncio
import time


class Exporter:
    def __init__(self, scrape_id):
        self.scrape_id = scrape_id

    async def run(self):
        loader = DataLoader(self.scrape_id)
        files, dfs = await loader.load()
        processor = Processor(files, dfs)
        await processor.process()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data exporter")
    parser.add_argument(
        "--scrape-id", type=str, required=True, help="ID of the scrape to export"
    )
    args = parser.parse_args()

    exporter = Exporter(scrape_id=args.scrape_id)
    asyncio.run(exporter.run())
