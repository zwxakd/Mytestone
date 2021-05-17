#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

#!/usr/bin/env python
# -*-coding:utf-8-*-

# Author:Zhangwx

from API_test_project.Common.Resuqet import RequestsHandler,Apirequest
from API_test_project.Common.Assert import *
from API_test_project.Common.public import *
from API_test_project.Common.Logs import *
from API_test_project.Params.operation import Operation, ExcelVarles
import os,sys
import allure
import pytest

excel = Operation().modol_data('书籍管理系统')
obj = Apirequest()

# file = os.path.basename(sys.argv[0])#获取当前模块名
# log = Log(file)
# logger = log.Logger
# print(logger)

@allure.description('书籍管理系统测试结果')
@pytest.mark.parametrize('datas', excel)
def test_login_001(datas,getToken):
	headers = datas[ExcelVarles.headers]
	if len(str(headers).strip()) == 0:
		pass
	elif len(str(headers).strip()) >= 0:
		headers = json.loads(headers)
		headers['Authorization'] = str('JWT') + ' ' + getToken
		headers = headers
		# print(headers,type(headers))

	'''对params进行判空处理'''
	params = datas[ExcelVarles.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		params = params

	#断言封装
	case_code = int(datas[ExcelVarles.stadus_code])
	def case_result_assert(r):
		assert r.status_code == case_code
		assert datas[ExcelVarles.expect] in json.dumps(r.json(),ensure_ascii=False)

	def getUrl():
		return str(datas[ExcelVarles.caseUrl]).replace('{bookId}', readContent())

	#执行用例
	if datas[ExcelVarles.method] == 'get':
		if '/books' in datas[ExcelVarles.caseUrl]:
			r = obj.send_requests(method='get',url=datas[ExcelVarles.caseUrl],data=params,headers = headers)
			case_result_assert(r=r)
		elif '{bookId}' in datas[ExcelVarles.caseUrl]:
			r = obj.send_requests(method='get', url=getUrl(), data=params, headers=headers)
			# print(r.json(),type(r.json()))
			case_result_assert(r=r)

	elif datas[ExcelVarles.method] == 'post':
		r = obj.send_requests(method='post',url=datas[ExcelVarles.caseUrl],json=json.loads(params),
			headers=headers)
		writeContent(content=str(r.json()[0]['datas']['id']))
		case_result_assert(r=r)

	elif datas[ExcelVarles.method] == 'put':
		url = getUrl()
		r= obj.send_requests(method='put',url=url,json = json.loads(params),headers=headers)
		case_result_assert(r=r)

	elif datas[ExcelVarles.method] == 'delete':
		url = getUrl()
		r= obj.send_requests(method='delete',url=url,headers=headers)
		case_result_assert(r=r)

if __name__ == '__main__':
	'''执行并生成allure测试报告'''
	pytest.main(['-s','-v','test_login_book.py','--alluredir','./report/result'])
	import subprocess
	subprocess.call('allure generate report/result -o report/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html',shell=True)
