# encoding: utf-8
# @author: xiaotao
# @file: main_page.py
# @time: 2021/3/29 0:11
# @desc:主页面类

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
webdriver_path=os.path.join(os.path.dirname(__file__),'..','webdriver','chromedriver.exe')
from common.log_utils import logger
from common.base_page import BasePage
class MainPage(BasePage):
    def __init__(self,driver):
        # login_page=LoginPage()
        # login_page.input_username('test01')
        # login_page.input_password('newdream123')
        # login_page.click_login()
        # self.driver=login_page.driver #把login_page的对象转移到main_page
        # self.companyname_shwbox=self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        # self.myzone_menu=self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        # self.product_menu=self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        # self.username_showspan=self.driver.find_element(By.XPATH,'//span[@class="user-name"]')
        super().__init__(driver)
        self.myzone_menu={"element_name":"我的地盘",
                                 "locator_type":"xpath",
                                 "locator_value":"//h1[@id='companyname']",
                                 "timeout":5
                                }
        self.product_menu={"element_name":"产品模块",
                                 "locator_type":"xpath",
                                 "locator_value":"//li[@data-id='my']",
                                 "timeout":5
                                }
        self.username_showspan={"element_name":"登录员工名称",
                                 "locator_type":"xpath",
                                 "locator_value":"//li[@data-id='product']",
                                 "timeout":5
                                }
        self.companyname_shwbox={"element_name":"公司名称",
                                 "locator_type":"xpath",
                                 "locator_value":"//span[@class='user-name']",
                                 "timeout":5
                                }


    #操作
    def get_companyname(self): #获取公司名称
        value=self.get_text(self.companyname_shwbox)
        return value
    def go_myzone(self): #进入我的地盘
        self.cilck(self.go_myzone())

    def goto_product(self): #进入产品模块
        self.cilck(self.go_myzone())

    def get_username(self): #获取用户名
        value=self.get_text(self.username_showspan)
        return value

if __name__=='__main__':
    webdriver_path = os.path.join(os.path.dirname(__file__), '..', 'webdriver', 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=webdriver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.set_browser_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    companyname=MainPage(driver).get_companyname()
    username=MainPage(driver).get_username()
    print(companyname)
    print(username)