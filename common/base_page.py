# encoding: utf-8
# @author: xiaotao
# @file: base_page.py
# @time: 2021/3/31 0:09
# @desc:
import os
import time
from selenium import webdriver
from common.log_utils import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Chrome()

    #浏览器操作
    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url网站%s'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def get_tile(self):
        title=self.driver.title
        logger.info('获取网页标题,标题为%s'%title)

    def web_quit(self):
        time.sleep(3)
        self.driver.quit()
        logger.info('关闭当前网页')


        # self.username_inputbox={'element_name':'用户输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="account"]',
        #                         'timeout':5}
    #元素识别,传入一个元素的识别信息数据，去返回一个元素
    def find_element(self,element_info):
        locator_name=element_info['element_name']
        locator_type_name=element_info['locator_type']
        local_value_info=element_info['locator_value']
        local_timeout=element_info['timeout']
        if locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name =='xpath':
            locator_type=By.XPATH
        elif locator_type_name == 'css':
            locator_type=By.CSS_SELECTOR

        element=WebDriverWait(self.driver,local_timeout).until(lambda x:x.find_element(locator_type,local_value_info))
        logger.info('[%s]元素识别成功'%locator_name)
        return element
    #封装元素操作方法
    def cilck(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logger.info('[%s]点击'%element_info['element_name'])
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入数据:%s'%(element_info['element_name'],content))

    def get_text(self,element_info):
        element=self.find_element(element_info)
        content=element.text
        logger.info('[%s]获取元素文本信息:%s'%(element_info['element_name'],content))
        return content


