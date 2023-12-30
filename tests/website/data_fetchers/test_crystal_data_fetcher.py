import pytest
from snow_data_aggregator.website.data_fetchers.crystal_data_fetcher import CrystalDataFetcher

data_fetcher = CrystalDataFetcher()


def test_get_snowfall_12():
    assert data_fetcher.get_snowfall_12() == 100


def test_get_snowfall_24():
    assert data_fetcher.get_snowfall_24() == 200


def test_get_forecast():
    assert data_fetcher.get_forecast() == "It's gnarly out here!"


def test_fetch_data():
    data_fetcher.fetch_data()
    test_get_snowfall_12()
    test_get_snowfall_24()
    test_get_forecast()