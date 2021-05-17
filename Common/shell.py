#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

import subprocess

class Shell:
	@staticmethod
	def invoke(cmd):
		output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
		o = output.decode("utf-8")
		return o