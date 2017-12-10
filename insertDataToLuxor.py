#!/usr/bin/python
# coding=utf-8

import requests

# change range to console insert count
for item in range(0,1):

    username = 'luxor'
    password = 'dreamarts'

    CoreNames = ['admin_guide', 'board', 'custom', 'fa_schedule', 'guide', 'history-library', \
                 'history-share', 'insuite_test', 'library', 'ml', 'ns_board', 'reminder', 'report', \
                 'schedule', 'share', 'smart', 'todo', 'wflow', 'binder', 'document', 'document_item', \
                 'imp', 'process']

    for core in CoreNames:
        # change component&function to console core and method
        data = {
            "type": 1,
            "origin": "9",
            "id": item,
            "component": core,
            "function": "insert",
            "title": "福岡県庁 パフォーマンス障害　対応",
            "content": [
                "福岡県庁 パフォーマンス障害　対応本件、既にメールにて、VC側に連絡し、修正パッチ出荷まで対応頂いてます。現在、パートナー＆お客様向け報告書を作成するPhaseになっており、VC側で対応頂いてます。(現在までの経緯はインシデントを確認ください。)残タスク　・報告書完成させる(←VC現在対応中)　・報告書提出および訪問日程調整　・訪問によるご説明及び謝罪(訪問者：古田、門脇さん、張吉さん、大江さん）2014/02/05　11:50　志水本日の共有MTGより、障害対応としてはDAにボールがなくなった点を伺いました。別途メールポートレットに関して個別パッチリリースというタスクが残っていますが、本お問い合わせとは別件で登録して頂くとの事でしたので、本件はこれにてクローズとさせて頂きます。2014/1/29 10:35　モリモリ大量SESSION_UPDATEの件は1/29に再リリースします。対応方針：クラシックメーラ利用時、または文字コードがEUC-JPの場合、リリースモジュールは1/29昼までリリースバインダにアップします。今まで調査したもの。> 　・Ver2.4.0とVer3.3.3ではUIがかなり変わっており、Ver2.4.0 当時、ReleaseNote Ver3000によると、Ver3.0.0が下記の仕様変更あります↓--------------------------------------------19) ポートレット  「ポートレット更新」ボタンをクリックしたときに、各ポートレット単位で更新をできるように改善更新されないように改善をしました。--------------------------------------------メールポートレットの「メール確認」をタップしないの場合のrefresh iconのスタイルはpic-1のようです、「メール確認」をタップすると、refresh icon　は　pic -2 のようです（その上、refresh iconは動くできるのgifです）。これは仕様ですが、Ver3.0.0後のバージョン（検証したは3.1.0、3.2.0 、3.3.0 、3.3.3、3.3.4）で、このrefresh iconは動くできないになりました。これはこのただし、                        pic -1                      pic - 2以上。この上に記録されたバグの修正方法見つかった。diffは下記です。[root@el5enhance43 portal]# diff -u /home/DreamArts/insuite/js/portal/refresher.js /root/refresher.js"]
        }

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

        # change ip to console insert server
        # update_url = 'http://luxor-cjtest.m.diol.jp:10080/solr/update_luxor?'
        update_url = 'http://localhost:10080/solr/update_luxor?'
        headers = {"Content-Type": "application/json"}
        r = requests.post(update_url, data=data)
        print ("item_id:", item, "core:", core, "status:", r.text)