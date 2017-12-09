#coding=utf-8
import json
import requests

# get data from A server and insert it to B server

# change range to console insert count
for item in range(9,5050):
    # change ip to console catch date server
    select_url = 'http://10.2.2.67:10080/solr/document/select?q=id:"\%s"&wt=json&indent=true'%item
    r = requests.get(select_url, verify = False)

    select_num = r.json()['response']['numFound']
    if select_num == 0:
        continue
    #print item+":"+str(select_num)
    print item

    select_data = r.json()['response']['docs']

    del select_data[0]['stitle']

    # change component&function to console core and method
    select_data[0]['component'] = "document"
    select_data[0]['function'] = "insert"

    username = 'luxor'
    password = 'dreamarts'
    data = select_data[0]
    print data

    update_params = {"boost":1.0,"overwrite":"true","commitWithin":1000}

    # change ip to console insert server
    # update_url = 'http://luxor-cjtest.m.diol.jp:10080/solr/update_luxor?'
    update_url = 'http://localhost:10080/solr/update_luxor?'
    headers = {"Content-Type": "application/json"}
    r = requests.post(update_url, data=data)
    print r.text

