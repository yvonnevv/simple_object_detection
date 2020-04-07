# 目标检测简单框架

## 目录结构

```sh
|- simple-object-detection-server
    |- model  # 对象识别模型
    |- object_detection  # 对象识别核心逻辑，克隆自 Google Tensorflow Model
    |- resources  # 训练、识别、标签管理等接口
    |- slim  # 克隆自 Google Tensorflow Model
    |- utils  # 工具
```

> object_detection 中的 export_inference_graph.py 是修改过的，和 Google 原版有点区别

## 图片标注

## 本地开发

### 环境配置

> python版本：python 3(如3.6.5)

所有操作以 macOS 为例，其他系统类似。

#### 安装 pyenv - 类似前端的 nvm

这是 Python 的多版本管理工具，推荐安装

```sh
brew install pyenv
```

#### 安装 pyenv virtualenv

这是 Python 多环境管理工具，每个项目都能开创一个新的 Python 环境，这个环境里面可以安装很多依赖包，不影响其他环境，这是 Python 的依赖管理的形式，和 NPM 不同，每个环境都是全局的环境。

```sh
brew install pyenv-virtualenv
```

#### 创建一个项目单独的环境

```sh
# 创建指定基于特定python版本的虚拟环境
pyenv virtualenv 3.6.5 simple-object-detection
# 切换到 simple-object-detection 环境
pyenv activate simple-object-detection
```

> 如不存在对应的python版本的话，需要先手动安装，`pyenv install 3.7.5`（查看可以安装的python版本：`pyenv install --list | less`)
> 如果报错`IOError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/virtualenv.py'`, 则执行`sudo chown -R $USER /Library/Python/2.7`即可。
> 如果报错`Failed to activate virtualenv.`, 尝试执行一下脚本：
> ```sh
> eval "$(pyenv init -)"
> eval "$(pyenv virtualenv-init -)"
> ```
> 可能每次启动shell都需要执行一遍，建议在`~/.bashrc`里面添加上面两行，然后执行`source ~/.bashrc`

#### 退出/删除环境

```sh
# 退出当前环境
pyenv deactivate
# 删除环境
pyenv uninstall simple-object-detection

```

#### 安装依赖

```sh
pip install -r requirements.txt
pip install pycocotools
```

### 相关命令

#### 训练模型

```sh
python resources/convert.py
python resources/train.py
```

#### 预测模型

```sh
python resources/detection.py
```

#### 模型评估

```sh
python resources/convert.py valid
python resources/eval.py
```
