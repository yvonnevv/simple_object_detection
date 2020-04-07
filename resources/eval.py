import tensorflow as tf
import os
import shutil
import sys

sys.path.append(os.path.realpath('.'))

from utils.path_config import MAIN_CONFIG
from utils.add_slim import add_slim_to_path

def eval():
    '''
    供 Python 调用的方法
    '''
    import object_detection.legacy.eval
    from object_detection.legacy.eval import main

    type = 'ssd'
    ALGORITHM_CONFIG = MAIN_CONFIG[type]['config']
    VALID_DATA_PATH = MAIN_CONFIG[type]['valid_data']
    MODEL_PATH = MAIN_CONFIG[type]['train_model']

    if os.path.exists(VALID_DATA_PATH):
        shutil.rmtree(VALID_DATA_PATH)

    os.mkdir(VALID_DATA_PATH)

    argv = [  
        '--logtostderr', 
        '--checkpoint_dir=' + MODEL_PATH,
        '--pipeline_config_path=' + ALGORITHM_CONFIG,
        '--eval_dir=' + VALID_DATA_PATH
    ]

    print(argv)

    tf.app.run(
        main=main,
        argv=argv
    )

if __name__ == '__main__':
    add_slim_to_path()
    eval()
