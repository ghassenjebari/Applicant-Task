import os


# Settings for filestore
FILESTORE_PATH = "/usr/src/filestore"

API_ROOT_PATH = os.getenv('API_ROOT_PATH', '')

ENV_MODE = os.getenv('ENV_MODE')

if ENV_MODE not in ['DEV', 'PROD', 'DEMO']:
    raise ImportError(
        'ENV_MODE needs to be set to any of [\'DEV\', \'PROD\', \'DEMO\']')
