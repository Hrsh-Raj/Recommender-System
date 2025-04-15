#Entity is a return type of a function
from collections import namedtuple

DataIngestionConfig = namedtuple('DatasetConfig', ['dataset_download_url',
                                                   'raw_data_dir',
                                                   'ingested_dir'])