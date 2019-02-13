# coding=utf-8

import csv
import requests
import sys
import json

reload(sys)
sys.setdefaultencoding( "utf-8" )

csv_file = 'search_history.csv'
# export_solr_server = 'http://localhost:10080/solr/search_history/select?wt=json&indent=true&q=*:*&start=0&rows='
q = 'search_date:[* TO 2019-01-16T12:12:04Z]'
# q = '*:*'
export_solr_server = 'http://localhost:10080/solr/search_history/select?indent=on&q=' + q + \
                     '&sort=search_date asc&wt=json&rows='
import_solr_server = 'http://localhost:10080/solr/search_history/update?wt=json'

component_array = ["insuite_test_component",
                   "document_component",
                   "history-share_component",
                   "document_item_component",
                   "imp_component",
                   "smart_component",
                   "admin_guide_component",
                   "ns_board_component",
                   "library_component",
                   "wflow_component",
                   "share_component",
                   "binder_component",
                   "guide_component",
                   "ml_component",
                   "process_component",
                   "reminder_component",
                   "fa_schedule_component",
                   "custom_component",
                   "history-library_component",
                   "todo_component",
                   "schedule_component",
                   "report_component",
                   "board_component",
                   "cms_component"]

necessary_field_array = ["hidden",
                         "search_account",
                         "search_date",
                         "id",
                         "search_terms"
                         ]

all_field = necessary_field_array + component_array

username = 'luxor'
password = 'dreamarts'

data_count = 0

# 从Solr抽取数据，保存到csv文件中
def export_data_from_solr_to_csv():
    print("export_data_from_solr_to_csv start.")
    # get numfound
    select_url = export_solr_server + "1"
    r = requests.get(select_url, verify=False)

    select_num = r.json()['response']['numFound']
    if 0 != select_num:
        csvfile = open(csv_file, 'w')
        writer = csv.writer(csvfile)
        writer.writerow(necessary_field_array + component_array)

        select_url = export_solr_server + str(select_num)
        r = requests.get(select_url, verify=False)
        docs = r.json()['response']['docs']
        for doc in docs:
            row = transform_data(doc)
            writer.writerow(row)
        csvfile.close()
    r.close()
    global data_count
    data_count = select_num
    print("export_data_from_solr_to_csv finish.")


# 从csv文件中抽取数据保存到Solr中
def import_data_from_csv_to_solr():
    print("import_data_from_csv_to_solr start.")
    with open(csv_file) as f:
        reader = csv.reader(f)
        head_row = next(reader)
        i = 0
        for row in reader:
            i = i + 1
            row_dic = {}
            for field in necessary_field_array:
                row_dic[field] = row[all_field.index(field)]

            for field in component_array:
                if row[all_field.index(field)] != '0':
                    row_dic[field] = 1

            if i % 1000 == 0:
                print(str(i)+"/"+str(data_count) + " have been transferred.")

            # change ip to console insert server
            # update_url = 'http://luxor-cjtest.m.diol.jp:10080/solr/update_luxor?'
            # r = requests.post(import_solr_server, data=row_dic)
            # update_params = {"boost": 1.0, "overwrite": "true", "commitWithin": 1000}
            update_params = {}
            solrheaders = {"Content-Type": "application/json"}
            # json_row = json.dumps(row_dic)
            r = requests.post(import_solr_server, json=[row_dic], params=update_params, headers=solrheaders,
                              auth=(username, password))
            if r.status_code != 200:
                print("import_data_from_csv_to_solr fail.")
                break
        print(str(i) + "/" + str(data_count) + " have been transferred.")
    print("import_data_from_csv_to_solr finish.")


# 清空Solr服务器中指定功能的索引数据
# 2019-01-16T09:29:47Z
def purge_solr_data():
    print("purge_solr_data start.")
    url = "http://localhost:10080/solr/search_history/update/?stream.body=%3Cdelete%3E%3Cquery%3E" + q + "%3C/query%3E%3C" \
          "/delete%3E&commit=true "
    r = requests.get(url, verify=False)
    if r.status_code == 200:
        print("purge_solr_data success.")

    r.close()


def transform_data(doc):
    # doc.pop("_version_")
    # if "search_terms_copy" in doc:
    #     doc.pop("search_terms_copy")

    list_row = []

    for field in necessary_field_array:
        if field == "search_date":
            date = doc.get(field)
            if date.startswith('2019-12'):
                date = date.replace('2019-12', '2018-12')
            list_row.append(date)
        else:
            list_row.append(doc.get(field))

    for field in component_array:
        if doc.get(field) is not None:
            list_row.append(doc.get(field))
        else:
            value = doc.get(field.replace('_component', ''))
            if value is None:
                list_row.append(0)
            else:
                list_row.append(value)

    return list_row


if __name__ == '__main__':
    # deal data number
    export_data_from_solr_to_csv()
    purge_solr_data()
    import_data_from_csv_to_solr()

