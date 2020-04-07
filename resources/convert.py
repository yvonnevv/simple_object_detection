import os
import shutil
import sys

sys.path.append(os.path.realpath('.'))

from utils.path_config import ASSETS_PATH
from utils.path_config import ANNOTATIONS_PATH
from utils.path_config import IMAGES_PATH
from utils.path_config import IMAGES_FOLDER
from utils.path_config import PATH_LABEL_MAP
from create_pascal_tf_record import create as convert_to_tf_file

def convert(type):
    type_set = type if type == 'valid' else 'train'
    print('set', type_set)
    # 触发文件转换
    convert_to_tf_file(
        years = 'VOC2007', # 新增一项 不然会取不到第一项
        set = type_set,
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../' + type_set + '_assets/images')),
        output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../' + type_set + '_assets/' + type_set + '.record')),
        label_map_path = PATH_LABEL_MAP,
        annotations_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../' + type_set + '_assets/annotation'))
    )

if __name__ == '__main__':
    convert(sys.argv[-1])