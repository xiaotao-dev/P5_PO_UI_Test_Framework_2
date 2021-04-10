# encoding: utf-8
# @author: xiaotao
# @file: config_utils.py
# @time: 2021/4/8 0:15
# @desc:

import configparser
import os
configs_path=os.path.join(os.path.dirname(__file__),'..','config','config.ini')
class ConfigUtils():
    def __init__(self,cfg_path=configs_path):
        self.cfg_path=cfg_path
        self.cfg_obj=configparser.ConfigParser()
        self.cfg_obj.read(self.cfg_path,encoding='utf-8')
    @property
    def get_url(self):
        value=self.cfg_obj.get('default','url')
        return value

    @property
    def get_driver_path(self):
        value=self.cfg_obj.get('default','driver_path')
        return value
    @property
    def get_driver_name(self):
        value=self.cfg_obj.get('default','driver_name')
        return value
cfg=ConfigUtils()

if __name__=="__main__":
    print(cfg.get_url)
    print(cfg.get_driver_path)
    print(cfg.get_driver_name)