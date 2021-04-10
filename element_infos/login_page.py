# encoding: utf-8
# @author: xiaotao
# @file: login_page.py
# @time: 2021/3/18 23:42
# @desc:登录页面类
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.browser import Browser
webdriver_path=os.path.join(os.path.dirname(__file__),'..','webdriver','chromedriver.exe')

class LoginPage(BasePage):
    def __init__(self,driver):
        #self.driver=webdriver.Chrome(executable_path=webdriver_path)
        super().__init__(driver)
        # self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@name="account"]') #属性->页面上的控件
        # self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        # self.login_button=self.driver.find_element(By.XPATH,'//button[@id="submit"]')
        # self.keepLogin_checkbox=self.driver.find_element(By.XPATH,'//input[@name="keepLogin[]"]')
        self.elements=ElementDataUtils(module_name='login').get_element_info(page_name='login_page')
        self.username_inputbox=self.elements['username_inputbox']
        self.password_inputbox=self.elements['password_inputbox']
        self.login_button=self.elements['login_button']
        # self.username_inputbox={'element_name':'用户输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="account"]',
        #                         'timeout':5}
        #
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 5}
        #
        # self.login_button = {'element_name': '登录按钮',
        #                      'locator_type': 'xpath',
        #                      'locator_value': '//button[@id="submit"]',
        #                      'timeout': 5}
        #
        # self.keepLogin_checkbox = {'element_name': '记住密码复选框',
        #                            'locator_type': 'xpath',
        #                            'locator_value': '//input[@name="keepLogin[]"]',
        #                            'timeout': 5}



    def input_username(self,username): #方法->控件的操作
        self.input(self.username_inputbox,username)
        time.sleep(2)

    def input_password(self,password):
        self.input(self.password_inputbox,password)
        time.sleep(2)

    def click_login(self):
        self.cilck(self.login_button)
        time.sleep(2)
if __name__=='__main__':
    # webdriver_path = os.path.join(os.path.dirname(__file__), '..', 'webdriver', 'chromedriver.exe')
    # driver=webdriver.Chrome(executable_path=webdriver_path)
    driver=Browser().get_driver()
    login_page=LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.set_browser_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
