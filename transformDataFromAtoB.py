#coding=utf-8
import json
import requests
import copy

# get data from A server and insert it to B server

# change range to console insert count
for item in range(9,10):
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

    CoreNames = ['admin_guide', 'board', 'custom', 'fa_schedule', 'guide', 'history-library', \
                 'history-share', 'insuite_test', 'library', 'ml', 'ns_board', 'reminder', 'report', \
                 'schedule', 'share', 'smart', 'todo', 'wflow', 'binder', 'document', 'document_item', \
                 'imp', 'process']

    username = 'luxor'
    password = 'dreamarts'

    del select_data[0]['binder_id']

    for core in CoreNames:
        # change component&function to console core and method
        data = copy.deepcopy(select_data[0])

        data['component'] = core
        data['function'] = "insert"

        if core == 'library' or core == 'share' or core == 'history-share' or core == 'history-library':
            data["gid"] = "2000000"
            data["bid"] = "111"

        if core == 'library' or core == 'history-library':
            data["bid"] = "111"

        if core == 'ml':
            data["ml"] = "999"

        if core == 'fa_schedule':
            data["gid"] = "2000001"
            data["fid"] = "222"

        update_params = {"boost":1.0,"overwrite":"true","commitWithin":1000}

        # change ip to console insert server
        # update_url = 'http://luxor-cjtest.m.diol.jp:10080/solr/update_luxor?'
        update_url = 'http://localhost:10080/solr/update_luxor?'
        headers = {"Content-Type": "application/json"}
        r = requests.post(update_url, data=data, auth=(username, password))
        print ("item_id:",item ," core:",core," status:",r.text)


