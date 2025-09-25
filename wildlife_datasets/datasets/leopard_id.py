import os
import pandas as pd
from . import utils
from .datasets_wildme import DatasetFactoryWildMe

summary = {
    'licenses': 'Community Data License Agreement – Permissive',
    'licenses_url': 'https://cdla.dev/permissive-1-0/',
    'url': 'https://lila.science/datasets/leopard-id-2022/',
    'publication_url': None,
    'cite': 'botswana2022',
    'animals': {'leopard'},
    'animals_simple': 'leopards',
    'real_animals': True,
    'year': 2022,
    'reported_n_total': None,
    'reported_n_individuals': 430,
    'wild': True,
    'clear_photos': False,
    'pose': 'multiple',
    'unique_pattern': True,
    'from_video': False,
    'cropped': False,
    'span': 'unknown',
    'size': 8565,
}

class LeopardID2022(DatasetFactoryWildMe):
    summary = summary
    url = 'https://lilawildlife.blob.core.windows.net/lila-wildlife/wild-me/leopard.coco.tar.gz'
    archive = 'leopard.coco.tar.gz'

    @classmethod
    def _download(cls):
        utils.download_url(cls.url, cls.archive)

    @classmethod
    def _extract(cls):
        utils.extract_archive(cls.archive, delete=True)

    def create_catalogue(self) -> pd.DataFrame:
        return self.create_catalogue_wildme('leopard', 2022)
