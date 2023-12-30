from snow_data_aggregator.website.scraper_clients.crystal_scraper_client import CrystalScraperClient

client = CrystalScraperClient()


def test_scrape():
    client.scrape()
    assert not client.data
