from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from data_layer.data_layer import DataLayer, DataLayerIdentifier
from id_service.id_service import IdService
from scrape_config.scrape_config import ScrapeConfig
from id_service.data_layer_id_service import ParentIdentifier

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


# NOTE would be nice if we could constrain T to
Config = TypeVar('Config', bound='ScrapeConfig')


class ScrapeParentIdentifier(ParentIdentifier):
    # HACK aren't we super duper coupling our shit with this ParentIdentifier composition design pattern? We are kinda coupling all of our classes to a specific implementation of idService, or is it reasonable to assume that all implementations of IdService would need some ParentIdentifier?

    @staticmethod
    def get_parent_identifier() -> DataLayerIdentifier:
        return 'scrapes'


@dataclass(frozen=True)
class Scraper(ABC, Generic[Config]):
    parent_identifier = ScrapeParentIdentifier
    # id: Id

    @classmethod
    @abstractmethod
    def run_scrape(cls, id_service: IdService, data_layer: DataLayer, scrape_config: Config) -> None:
        raise NotImplementedError
