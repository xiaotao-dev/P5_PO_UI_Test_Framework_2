# encoding: utf-8
# @author: xiaotao
# @file: element_data_utils.py
# @time: 2021/4/2 1:34
# @desc:读取元素识别excel中的信息工具模块
import os
import xlrd
excel_path=os.path.join(os.path.dirname(__file__),'..','element_info_datas/element_info_datas.xlsx')

class ElementDataUtils(object):
    def __init__(self,module_name,element_path=excel_path):
        self.element_path=element_path
        self.work_book = xlrd.open_workbook(self.element_path)
        self.sheet = self.work_book.sheet_by_name(module_name)
        #self.page_name=page_name
        self.row_count = self.sheet.nrows  # 求行数
    def get_element_info(self,page_name):
        elements_infos = {}
        for i in range(1, self.row_count):  # row_count=4 取1、2、3行
            if self.sheet.cell_value(i,2)==page_name:
                elements_info = {}
                elements_info['element_name'] = self.sheet.cell_value(i, 1)
                elements_info['locator_type'] = self.sheet.cell_value(i, 3)
                elements_info['locator_value'] = self.sheet.cell_value(i, 4)
                elements_info['timeout'] = self.sheet.cell_value(i, 5)
                elements_infos[self.sheet.cell_value(i, 0)] = elements_info
        return elements_infos

if __name__=='__main__':
    elements=ElementDataUtils(module_name='login').get_element_info(page_name='login_page')
    print(elements)
    for element in elements.keys():
        print(elements,elements[element])
