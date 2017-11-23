#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import threading
from time import sleep, ctime

url = 'https://xxx/hibiki/BRDDocument.do'


headers = {

    }

def insert_data(data):

    username = 'luxor'
    password = 'dreamarts'
    update_params = {"boost": 1.0, "overwrite": "true", "commitWithin": 1000}
    update_url = 'http://localhost:10080/solr/document/update?wt=json?'
    solrheaders = {"Content-Type": "application/json"}
    r = requests.post(update_url, json=data, params=update_params, headers=solrheaders, auth=(username, password))

    print r.text


def getMoeDataTo20(start,end):

    for i in range(start,end):
        print i

        querystring = {"func":"simpleView","binderId":"14979","recordId":i}
        response = requests.request("GET", url, headers=headers, params=querystring)

        content = response.content
        tr = etree.HTML(content)
        title = ""
        if len(tr.xpath('//*[@id="i14131_10089_view-mode"]//div')) > 0:
            title = tr.xpath('//*[@id="i14131_10089_view-mode"]//div')[0].text
        else:
            continue
        print title

        j = 0;
        text = ""
        while (j < len(tr.xpath('//p'))):
            if tr.xpath('//p')[j].text == None:
                pass
            else:
                text = text + tr.xpath('//p')[j].text
            j = j + 1

        # text = re.sub(r'{', "", text)
        # text = re.sub(r'}', "", text)

        print text

        data = {
            "add": {
                "doc": {
                    "title": title,
                    "content": title + text,
                    "binder_id": 12609,
                    "id": i,
                }
            }
        }

        insert_data(data)

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def main():
    print 'Starting at:', ctime()

    max_num_thread = 5
    threads = []

    nloops = range(max_num_thread)

    for i in nloops:
        # 调用ThreadFunc类实例化的对象，创建所有线程
        start = i*505
        end = start + 505
        t = threading.Thread(
            target=ThreadFunc(getMoeDataTo20, (start,end), getMoeDataTo20.__name__)
        )
        threads.append(t)

    # 开始线程
    for i in nloops:
        threads[i].start()

    # 等待所有结束线程
    for i in nloops:
        threads[i].join()

    print 'All end:', ctime()


if __name__ == '__main__':
    main()
