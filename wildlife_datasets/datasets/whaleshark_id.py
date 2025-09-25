import pandas as pd
from . import utils
from .datasets_wildme import DatasetFactoryWildMe

summary = {
    'licenses': 'Community Data License Agreement – Permissive',
    'licenses_url': 'https://cdla.dev/permissive-1-0/',
    'url': 'https://lila.science/datasets/whale-shark-id',
    'publication_url': 'https://www.int-res.com/abstracts/esr/v7/n1/p39-53/',
    'cite': 'holmberg2009estimating',
    'animals': {'whale shark'},
    'animals_simple': 'sharks',
    'real_animals': True,
    'year': 2020,
    'reported_n_total': 7693,
    'reported_n_individuals': 543,
    'wild': True,
    'clear_photos': False,
    'pose': 'multiple',
    'unique_pattern': True,
    'from_video': False,
    'cropped': False,
    'span': '5.2 years',
    'size': 6466,
}

class WhaleSharkID(DatasetFactoryWildMe):
    summary = summary
    url = 'https://lilawildlife.blob.core.windows.net/lila-wildlife/wild-me/whaleshark.coco.tar.gz'
    archive = 'whaleshark.coco.tar.gz'

    @classmethod
    def _download(cls):
        utils.download_url(cls.url, cls.archive)

    @classmethod
    def _extract(cls):
        utils.extract_archive(cls.archive, delete=True)

    def create_catalogue(self) -> pd.DataFrame:
        return self.create_catalogue_wildme('whaleshark', 2020)
