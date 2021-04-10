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
        #self.driver=driver
        self.driver=webdriver.Chrome()

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

    # 思路1：通过元素来切
    def switch_to_frame(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路2：通过id或者name来切
    def switch_to_frame_by_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_frame_by_element(self,element_info):
        element=self.driver.find_element(element_info)
        self.driver.switch_to.frame(element)
    # 思路3：灵活处理，把识别的方法做成收集参数
    #id=frameid name=framename element=element_info
    def switch_to_frame(self,**element_dict):#switch_to_frame(id=frmaid)
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])

        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])

        elif 'element' in element_dict.keys():
            element=self.driver.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)
    #js='arguments[0].removeAttribute(‘value’)'移除元素的value属性
    # js='arguments[0].setAttribute('value','newdream')移除元素的value属性

    def delete_element_attribute(self,element_info,attribute):
        pass

    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element=self.driver.find_element(element_info)
        js="arguments[0].setAttribute('value','newdream')"