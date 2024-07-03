import kaggle
import os
import shutil

def download_dataset(dataset_name = 'nbroad/fluorescent-neuronal-cells'):
    kaggle.api.authenticate()
    try:
        shutil.rmtree('data')
    except:
        pass
    os.mkdir('data')
    kaggle.api.dataset_download_files(dataset_name, path='data', unzip=True)

