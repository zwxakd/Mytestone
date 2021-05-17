#!/usr/bin/env python
#-*-coding:utf-8-*-

#Author:Zhangwx

from Params.operation import *
from Common.Resuqet import RequestsHandler,Apirequest
import pytest,json

excel = Operation().case_pre(ExcelVarles.casePre)
res = RequestsHandler()
@pytest.fixture(scope='module')
def getToken():
	url = 'http://127.0.0.1:5000/auth'
	data = {"username":"wuya","password":"asd888"}
	r=res.post_Req(url=url,json=data)
	return r.json()['access_token']



