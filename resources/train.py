import tensorflow as tf
import os
import shutil
import sys

sys.path.append(os.path.realpath('.'))

from utils.path_config import MAIN_CONFIG
from utils.path_config import PATH_TRAIN_DATA
from utils.add_slim import add_slim_to_path

def train():
    '''
    供 Python 调用的方法
    '''
    import object_detection.legacy.train
    from object_detection.legacy.train import main
    
    ALGORITHM_CONFIG_PATH = MAIN_CONFIG['ssd']['config']
    TRAIN_DATA_PATH = MAIN_CONFIG['ssd']['train_data']

    if os.path.exists(TRAIN_DATA_PATH):
        shutil.rmtree(TRAIN_DATA_PATH)

    os.mkdir(TRAIN_DATA_PATH)

    argv = [
        '--logtostderr',
        '--pipeline_config_path=' + ALGORITHM_CONFIG_PATH,
        '--train_dir=' + TRAIN_DATA_PATH
    ]

    print(argv)

    tf.app.run(
        main=main,
        argv=argv
    )

if __name__ == '__main__':
    add_slim_to_path()
    train()