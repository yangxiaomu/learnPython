#!/usr/bin/python
# coding=utf-8

import requests

url = 'http://localhost:10080/solr/update_luxor?'

data = { "doc":{"id":"100001","title":u"我是一个大好人","component":"ns_board"}}
params = {"boost":1.0,"overwrite":"true","commitWithin":1000}

headers = {"Content-Type": "application/json"}
r = requests.post(url, params = data, headers = headers)
print r.text