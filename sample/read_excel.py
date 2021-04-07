# encoding: utf-8
# @author: xiaotao
# @file: read_excel.py
# @time: 2021/4/2 1:16
# @desc:读取excel
import xlrd
import os
excel_path=os.path.join(os.path.dirname(__file__),'..','element_info_datas/element_info_datas.xlsx')

work_book=xlrd.open_workbook(excel_path)
sheet=work_book.sheet_by_name('login_page')
row_count=sheet.nrows #求行
#username_inputbox={'element_name':'用户输入框',
                                #'locator_type':'xpath',
                                #'locator_value':'//input[@name="account"]',
                                #'timeout':5}
elements_infos={}
for i in range(1,row_count):  #row_count=4 取1、2、3行
    elements_info={}
    elements_info['element_name']=sheet.cell_value(i,1)
    elements_info['locator_type']=sheet.cell_value(i,2)
    elements_info['locator_value']=sheet.cell_value(i,3)
    elements_info['locator_value']=sheet.cell_value(i,4)
    elements_infos[sheet.cell_value(i,0)]=elements_info

print(elements_infos)
for i in elements_infos:
    print(i,elements_infos[i])