#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import threading
from time import sleep, ctime

# it is a spider for catch moe document content to index


url = 'https://xxx/hibiki/BRDDocument.do'

headers = {

    }

catch_count = 0
insert_count = 0

def insert_data(data):

    username = 'luxor'
    password = 'dreamarts'
    update_params = {"boost": 1.0, "overwrite": "true", "commitWithin": 1000}
    update_url = 'http://xxx:port/solr/update_luxor?'
    solrheaders = {"Content-Type": "application/json"}
    r = requests.post(update_url, json=data, params=data, headers=solrheaders, auth=(username, password))

    print r.text

    global insert_count
    insert_count += 1

def getMoeDataTo1_3(start,end):

    for i in range(start,end):

        print ("deal id:",i)
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

        global  catch_count
        catch_count += 1

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
            "title": title,
            "content": title + text,
            "binder_id": 12609,
            "id": i,
            "component":"document",
            "function":"document"
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

    max_num_thread = 1
    threads = []

    nloops = range(max_num_thread)

    for i in nloops:
        # 调用ThreadFunc类实例化的对象，创建所有线程
        #start = i*505
        #end = start + 505
        start = 4925
        end = 4927
        t = threading.Thread(
            target=ThreadFunc(getMoeDataTo1_3, (start,end), getMoeDataTo1_3.__name__)
        )
        threads.append(t)

    # 开始线程
    for i in nloops:
        threads[i].start()

    # 等待所有结束线程
    for i in nloops:
        threads[i].join()

    print ("catch_count:", catch_count)
    print ("insert_count", insert_count)

    print 'All end:', ctime()


if __name__ == '__main__':
    main()


