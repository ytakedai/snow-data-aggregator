from abc import ABC, abstractmethod


class ScraperClientInterface(ABC):

    def __init__(self):
        self.data = self.scrape()

    @abstractmethod
    def scrape(self):
        pass

