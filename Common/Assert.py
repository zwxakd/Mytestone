#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

import pytest,json
from Common.Logs import Log

class Assertion(Log):
	def __int__(self,def_name):
		self.def_name = def_name
		log = Log(def_name)
		self.logger = log.Logger

	def assert_code(self,code,expected_code):
		'''
		验证返回值的状态码
		:param  code
		:
		:return:
		'''
		try:
			assert code == expected_code
			self.logger.info('业务状态码验证正确，预期返回值为{0}，实际返回值为{1}',format(expected_code,code))
		except:
			self.logger.error('业务状态码验证错误，预期返回值为{0}，实际返回值为{1}',format(expected_code,code))
			raise
	def assert_body(self,body,body_msg,expected_msg):
		'''
		验证response中任意属性的值
		:param body:
		:param body_msg:
		:param expected_msg:
		:return:
		'''
		try:
			assert body[body_msg] == expected_msg
			self.logger.info('响应数据部分值与实际返回值相同，期望返回值为{0}，实际返回值为{1}',format(expected_msg,body[body_msg]))
		except:
			self.logger.error('响应数据部分值与实际返回值不同，期望返回值为{0}，实际返回值为{1}',format(expected_msg,body[body_msg]))
			raise
	def assert_in_text(self,body,expected_msg):
		'''
        验证response body中是否包含预期字符串
		:param body:
		:param expected_msg:
		:return:
		'''
		try:
			text = json.dumps(body,ensure_ascii=False)
			assert  expected_msg in text
			self.logger.info('响应数据验证正确，期望返回值为{0},实际返回值为{1}',format(expected_msg,body))
		except:
			self.logger.error('响应数据验证错误，期望返回值为{0},实际返回值为{1}',format(expected_msg,body))
			raise

	def assert_text(self,body,expected_msg):
		'''
		验证response body中是否等于预期字符串
		:param body:
		:param expected_msg:
		:return:
		'''
		try:
			assert body == expected_msg
			self.logger.info('响应数据验证正确，期望返回值为{0},实际返回值为{1}',format(expected_msg,body))
		except:
			self.logger.error('响应数据验证错误，期望返回值为{0},实际返回值为{1}',format(expected_msg,body))
			raise

	def assert_time(self, time, expected_time):
		"""
		验证response body响应时间小于预期最大响应时间,单位：毫秒
		:param body:
		:param expected_time:
		:return:
		"""
		try:
			assert time < expected_time
		# return True

		except:
			self.logger.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
			raise