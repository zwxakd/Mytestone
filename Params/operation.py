#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

import xlrd,pytest,json
from API_test_project.Common.public import *

class ExcelVarles:
    caseId = '测试用例ID'
    caseModel = '模块'
    caseName = '接口名称'
    caseUrl = '请求地址'
    casePre = '前置条件'
    method = '请求方法'
    pramasType = '请求参数类型'
    params = '请求参数'
    expect = '期望结果'
    isRun = '是否运行'
    headers = '请求头'
    stadus_code = '状态码'

class Operation:
    def getSheet(self):
        book = xlrd.open_workbook(filePath())
        return book.sheet_by_index(0)#根据索引获取到sheet表

    def getExceldata(self):
        datas = list()
        title = self.getSheet().row_values(0)
        for row in range(1,self.getSheet().nrows):
            rowvalue = self.getSheet().row_values(row)
            datas.append(dict(zip(title,rowvalue)))
        return datas

    def runs(self):
        '''获取执行的测试用例'''
        run_list = list()
        for item in self.getExceldata():
            if str(item[ExcelVarles.isRun]).strip()=='y':
                run_list.append(item)
            else:pass
        return run_list

    def casedata(self):
        '''获取所有的测试用例'''
        case_list = list()
        for item in self.getExceldata():
            case_list.append(item)
        return case_list

    def params_dict(self):
        '''对请求参数进行判空处理'''
        params_list = []
        for item in self.runs():
            params = item[ExcelVarles.params]
            if len(str(params).strip()) == 0:params_list.append(params)
            elif len(str(params).strip())>= 0:
                params = json.loads(params)
                params_list.append(params)
        return params_list

    def modol_data(self,mark_name):
        '''
        根据模块名称获取测试用例
        :param mark_name:模块名称
        :return:
        '''
        mark_list = []
        for item in self.runs():
            if mark_name in item[ExcelVarles.caseModel]:
                mark_list.append(item)
            else:pass
        return mark_list

    def case_pre(self,casepre):
        '''
        根据前置条件获取用例
        :param casepre: 前置条件名称
        :return:
        '''
        for item in self.casedata():
            if casepre == item[ExcelVarles.caseId]:
                return item
        return None

# #调试代码
if __name__ == '__main__':
    r=Operation()
    for item in r.casedata():
        print(item)