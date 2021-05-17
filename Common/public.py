#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

import os

os.path.dirname(__file__)#获取当前目录
os.path.dirname(os.path.dirname(__file__))#获取当前目录的上一级

#获取指定目录
def fileDir(data):
	'''

	:param data:目录
	:return:返回
	'''
	base_path = os.path.dirname(os.path.dirname(__file__))
	return os.path.join(base_path,data)#将获取到的目录返回

#获取路径下的文件，调用需要传入两个参数替换，否则使用默认参数
def filePath(fileDir = 'Params',fileName = 'testCase.xls'):
	'''

	:param fileDir:目录
	:param fileName:文件名称
	:return:返回
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)
# print(filePath('Params','Login.yaml'))
def writeContent(content):
	with open(filePath(fileDir='Params',fileName='bookid'),'w') as f:
		return f.write(str(content))

def readContent():
	with open(filePath(fileDir='Params',fileName='bookid'),'r') as f:
		return f.read()




