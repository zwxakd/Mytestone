#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

import yaml
import os,json,pytest

class Readconf:
	'''获取config文件数据（列表数据类型）'''
	def get_confdata(self):
		confpath = os.path.join(os.path.dirname(__file__),'config.yaml')
		with open(confpath,'r',encoding='utf-8') as f:
			self.r = f.read()
			# conf_data = yaml.load(self.r,Loader = yaml.FullLoader)#字典类型
			conf_data = list(yaml.safe_load_all(self.r))#字符串类型
			return conf_data

#调试代码
# r= Readconf().get_confdata()
# print(r,type(r))
# for item in r:
# 	print(item,type(item))
class Test_login(Readconf):
	dictyaml = Readconf()
	@pytest.mark.parametrize('datas',dictyaml.get_confdata())
	def test_login_001(self,datas):
		return datas


if __name__ == '__main__':pytest.main(['-s','-v','Test_login::test_login_001'])