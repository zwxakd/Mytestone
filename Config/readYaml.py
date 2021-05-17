#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

from API_test_project.Common.public import *
import yaml

class OperationYaml():
	# def __int__(self):
	# 	self.filepath = filePath()

	def readYaml(self):
		with open(filePath(),'r',encoding='utf-8') as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self,fileDir='Params',fileName='login.yaml'):
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
			return yaml.safe_load(f)
