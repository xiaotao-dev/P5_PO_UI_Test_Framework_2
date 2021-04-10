# encoding: utf-8
# @author: xiaotao
# @file: demo1.py
# @time: 2021/4/8 23:19
# @desc:
str1='bug标题:%s'
title='阿信自动化31938'
print('bug标题:%s'%title)
print(str1%title)
str2=str1%title
print(str2)

from common.element_data_utils import ElementDataUtils
element=ElementDataUtils('login').get_element_info('bug_page')
print(element)
bug_link=element['bug_link']
element_name=bug_link['element_name']%title
locator_type=bug_link['locator_type']
locator_value=bug_link['locator_value']%title
timeout=bug_link.get('timeout')
print(element_name)
print(locator_value)
print(timeout)
