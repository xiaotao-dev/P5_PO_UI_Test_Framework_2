# encoding: utf-8
# @author: xiaotao
# @file: config_demo1.py
# @time: 2021/4/7 23:56
# @desc:
import configparser
import os
configs_path=os.path.join(os.path.dirname(__file__),'..','config','config.ini')
print(configs_path)
cfg_obj=configparser.ConfigParser()
cfg_obj.read(configs_path,encoding='utf-8')
url=cfg_obj.get('default','url')
print(url)