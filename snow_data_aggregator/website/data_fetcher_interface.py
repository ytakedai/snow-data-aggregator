from abc import ABC, abstractmethod


class DataFetcherInterface(ABC):

    @abstractmethod
    def get_snowfall_12(self) -> int:
        pass

    @abstractmethod
    def get_snowfall_24(self) -> int:
        pass

    @abstractmethod
    def get_forecast(self) -> str:
        pass

    @abstractmethod
    def fetch_data(self) -> str:
        pass
