import tensorflow as tf
import os
import shutil

from utils.path_config import MAIN_CONFIG
from utils.helper import get_value

def get_checkpoint_path(type):
    TRAIN_DATA_PATH = MAIN_CONFIG[type]['train_data']
    CHECKPOINT_PATH = os.path.join(TRAIN_DATA_PATH, 'checkpoint')
    
    with open(CHECKPOINT_PATH, 'r') as checkpoint_file:
        line = checkpoint_file.readline()
        file_name = line.split('/').pop().replace('"', '').replace('\n', '')
        file_path = os.path.join(TRAIN_DATA_PATH, file_name)
        return file_path

def export(*args):
    '''
    供 Python 调用的方法
    '''
    print('==========')
    import object_detection.export_inference_graph
    from object_detection.export_inference_graph import main
    type = get_value('algorithm')

    ALGORITHM_CONFIG_PATH = MAIN_CONFIG[type]['config']
    TRAIN_MODEL_PATH = MAIN_CONFIG[type]['train_model']

    print('TRAIN_MODEL_PATH', TRAIN_MODEL_PATH)

    if os.path.exists(TRAIN_MODEL_PATH):
        shutil.rmtree(TRAIN_MODEL_PATH)

    os.mkdir(TRAIN_MODEL_PATH)

    argv = [
        '--pipeline_config_path=' + ALGORITHM_CONFIG_PATH,
        '--trained_checkpoint_prefix=' + get_checkpoint_path(type),
        '--output_directory=' + TRAIN_MODEL_PATH
    ]

    print(argv)

    tf.app.run(
        main=main,
        argv=argv
    )


