#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx
#!/usr/bin/python
# -*- coding: UTF-8 _*_

import allure,pytest

if __name__ == '__main__':
	'''执行并生成allure测试报告'''
	pytest.main(['-s','-v','test_login_book.py','--alluredir','./report/result'])
	import subprocess
	subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html',shell=True)