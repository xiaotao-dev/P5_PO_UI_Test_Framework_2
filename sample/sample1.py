# encoding: utf-8
# @author: xiaotao
# @file: sample1.py
# @time: 2021/4/2 0:18
# @desc:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,element_info):
        locator_name=element_info['element_name']
        local_type=element_info['locator_type']
        local_value=element_info['local_value']
        time_out=element_info['time_out']
        if local_type=='name':
            local_type_name=By.NAME
        elif local_type=='css':
            local_type_name=By.CSS_SELECTOR
        elif local_type=='xpath':
            local_type_name=By.XPATH

        element=WebDriverWait(self.driver,time_out).until(lambda x:x.find_element(local_type_name,local_value))
        return element