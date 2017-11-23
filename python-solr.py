#coding=utf-8
import json
import requests



for item in range(0,5050):
    select_url = 'http://10.2.2.67:10080/solr/document/select?q=id:"\%s"&wt=json&indent=true'%item
    r = requests.get(select_url, verify = False)

    select_num = r.json()['response']['numFound']
    if select_num == 0:
        continue
    #print item+":"+str(select_num)

    select_data = r.json()['response']['docs']
    print select_data
    #del select_data[0]['_version_']
    del select_data[0]['stitle']

    username = 'luxor'
    password = 'dreamarts'
    data = select_data
    update_params = {"boost":1.0,"overwrite":"true","commitWithin":1000}
    update_url = 'http://10.2.8.201:10080/solr/document/update?wt=json'
    headers = {"Content-Type": "application/json"}
    r = requests.post(update_url, json = data, params = update_params, headers = headers,auth=(username, password))
    print r.text



# data = {
#     "add": {
#         "doc": {
#             "type": 1,
#             "owner": [
#                 "1000011"
#             ],
#             "origin": "145-1000011-201704-6",
#             "id": "145-1000011-201704-6",
#             "title": "python",
#             "content": [
#                 "test123"
#             ],
#             "reg_account": 1000011
#         }
#     }
# }

# update_params = {"boost":1.0,"overwrite":"true","commitWithin":1000}
# update_url = 'http://127.0.0.1:10080/solr/ns_board/update?wt=json'
# headers = {"Content-Type": "application/json"}
# r = requests.post(update_url, json = data, params = update_params, headers = headers)
# print r.text