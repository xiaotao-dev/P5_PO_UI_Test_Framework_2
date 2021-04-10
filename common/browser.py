# encoding: utf-8
# @author: xiaotao
# @file: browser.py
# @time: 2021/4/8 0:28
# @desc:二次封装
import os
from selenium import webdriver
from common.config_utils import cfg
from selenium.webdriver.chrome.options import Options
dri_path=os.path.join(os.path.dirname(__file__),'..',cfg.get_driver_path)
class Browser():
    def __init__(self,driver_path=dri_path,driver_name=cfg.get_driver_name):
        self.__driver_path=driver_path
        self.__driver_name=driver_name

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path=os.path.join(self.__driver_path,'chromedriver.exe')
        driver=webdriver.Chrome(executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path=os.path.join(self.__driver_path,'geckodriver.exe')
        dirver=webdriver.Firefox(executable_path=firefox_driver_path)
        return dirver

    def get_driver(self):
        if self.__driver_name.lower()=='chrome':
            return self.__get_chrome_driver()
        elif self.__driver_name.lower()=='firefox':
            return self.__get_firefox_driver()
    #分布式，远程的浏览器驱动 要求:3台电脑分布式并发执行，每台电脑执行不同的浏览器跑用一套脚本
    def __get__remoter_driver(self):#selenium支持分布式执行grid 扩展：自己完事代码
        pass
if __name__=="__main__":
    dirver=Browser().get_driver()
    dirver.get('https://www.baidu.com')