from snow_data_aggregator.website.data_fetcher_interface import DataFetcherInterface
from snow_data_aggregator.website.scraper_clients.crystal_scraper_client import CrystalScraperClient


class CrystalDataFetcher(DataFetcherInterface):
    def __init__(self):
        super().__init__()
        self.scraper = CrystalScraperClient()

    def get_snowfall_12(self) -> int:
        # return self.scraper.data._____
        return 100

    def get_snowfall_24(self) -> int:
        return 200

    def get_forecast(self) -> str:
        return "It's gnarly out here!"

    def fetch_data(self):
        self.scraper.scrape()
