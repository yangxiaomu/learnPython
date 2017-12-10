#coding=utf-8
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# search test:get data from A server and test it to B server

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
    title = select_data[0]['title']

    CoreNames = ['admin_guide', 'board', 'custom', 'fa_schedule', 'guide', 'history-library', \
                 'history-share', 'insuite_test', 'library', 'ml', 'ns_board', 'reminder', 'report', \
                 'schedule', 'share', 'smart', 'todo', 'wflow', 'binder', 'document', 'document_item', \
                 'imp', 'process']

    # CoreNames = ['document']

    username = 'luxor'
    password = 'dreamarts'

    for core in CoreNames:

        print ("=================")
        # qString = '(((title:'+ title + ' OR content:' + title + ')))';
        qString = 'title:' + title;

        data = {
            "component":core,
            "q":qString,
            "login_id":1000011
        }

        # change ip to console insert server
        # update_url = 'http://luxor-cjtest.m.diol.jp:10080/solr/update_luxor?'

        ## luxor api,the permit check is needed
        #update_url = 'http://localhost:10080/solr/select?wt=json&indent=true'

        # solr api
        update_url = 'http://localhost:10080/solr/'+core+'/select?wt=json&indent=true'
        headers = {"Content-Type": "application/json"}
        r = requests.post(update_url, data=data, auth=(username, password))
        select_num = r.json()['response']['numFound']
        if select_num == 0:
            print ("Search Failed:item", item, " core:", core, " q:")
            print qString.decode('utf-8')
            continue

        print ("Search Success: item_id:",item ," core:",core," numFound:",select_num)

