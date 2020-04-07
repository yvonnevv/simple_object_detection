import os

PATH_CONFIG = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config'))
# 算法配置
PATH_SSD_CONFIG = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/ssd_mobilenet_v1_coco.config'))
PATH_FAST_RCNN_CONFIG = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/faster_rcnn_inception_v2_coco.config'))

# 算法模板
PATH_SSD_TEMPLATE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/ssd_mobilenet_v1_coco.config'))
PATH_FAST_RCNN_TEMPLATE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates/faster_rcnn_inception_v2_coco.config'))

# label_map
PATH_LABEL_MAP = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/label_map.pbtxt'))

# fine_tune_checkpoint
PATH_SSD_FINE_TUNE_CHECKPOINT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/ssd_mobilenet_v1_coco_2017_11_17/model.ckpt'))
PATH_FAST_RCNN_FINE_TUNE_CHECKPOINT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt'))

# 数据集
PATH_TRAIN_ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), '../train_assets'))
PATH_VALID_ASSETS = os.path.abspath(os.path.join(os.path.dirname(__file__), '../valid_assets'))

# 训练/模型相关
PATH_TRAIN_DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), '../train_data'))
PATH_TRAIN_MODEL = os.path.abspath(os.path.join(os.path.dirname(__file__), '../train_model'))
PATH_VALID_DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), '../valid_data'))

# 预测
PATH_DETECTION = os.path.abspath(os.path.join(os.path.dirname(__file__), '../train_detections'))

IMAGES_FOLDER = 'images'
ANNOTATIONS_FOLDER = 'annotations'
# 训练资源存放地址
ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../train_assets'))
# 图片地址
IMAGES_PATH = os.path.abspath(os.path.join(ASSETS_PATH, 'assets/images/' + IMAGES_FOLDER))
# 标注数据地址
ANNOTATIONS_PATH = os.path.abspath(os.path.join(ASSETS_PATH, ANNOTATIONS_FOLDER))

# 验证资源存放地址
ASSETS_PATH_VALID = os.path.abspath(os.path.join(os.path.dirname(__file__), '../valid_assets'))
# 验证图片地址
IMAGES_PATH_VALID = os.path.abspath(os.path.join(ASSETS_PATH_VALID, 'assets/images/' + IMAGES_FOLDER))
# 验证标注数据地址
ANNOTATIONS_PATH_VALID = os.path.abspath(os.path.join(ASSETS_PATH_VALID, ANNOTATIONS_FOLDER))

MAIN_CONFIG = {
    'ssd': {
        'template': PATH_SSD_TEMPLATE,
        'config': PATH_SSD_CONFIG,
        'fine_tune_checkpoint': PATH_SSD_FINE_TUNE_CHECKPOINT,
        'train_data': os.path.abspath(os.path.join(PATH_TRAIN_DATA, './ssd')),
        'valid_data': os.path.abspath(os.path.join(PATH_VALID_DATA, './ssd')),
        'train_model': os.path.abspath(os.path.join(PATH_TRAIN_MODEL, './ssd')),
    },
    'fast_rcnn': {
        'template': PATH_FAST_RCNN_TEMPLATE,
        'config': PATH_FAST_RCNN_CONFIG,
        'fine_tune_checkpoint': PATH_FAST_RCNN_FINE_TUNE_CHECKPOINT,
        'train_data': os.path.abspath(os.path.join(PATH_TRAIN_DATA, './fast_rcnn')),
        'valid_data': os.path.abspath(os.path.join(PATH_VALID_DATA, './fast_rcnn')),
        'train_model': os.path.abspath(os.path.join(PATH_TRAIN_MODEL, './fast_rcnn')),
    }
}