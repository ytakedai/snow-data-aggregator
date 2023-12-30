from snow_data_aggregator.website.scraper_client_interface import ScraperClientInterface


class CrystalScraperClient(ScraperClientInterface):

    def scrape(self):
        self.__scrape_data()

    def __scrape_data(self):
        self.data = None
