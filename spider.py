#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-10-03 23:23:13
# Project: news

from pyspider.libs.base_handler import *
from pyspider.database.mysql.SQL import SQL

class Handler(BaseHandler):
    url_list = ["http://www.chinadaily.com.cn/business/money_"+str(i)+".html" for i in range(30, 100, 1)]
    sql = SQL()

    def on_start(self):
        for url in self.url_list:
            self.crawl(url, callback=self.index_page)

    def index_page(self, response):
        for each in response.doc('div.busBox1').items():
            item = {
                'url': each('h3>a').attr.href,
                'title': each('h3>a').text(),
                'time': each('div>span').text().strip('[]'),
            }
            self.sql.add('newsinfo', **item)
            print item["time"]
            self.crawl(item["url"], callback=self.detail_page)

    def detail_page(self, response):
        item = response.doc('div.pt30')
        text = ""
        for line in item('p').items():
            text = text + line.text() + '\n'
        return {
            "url": response.url,
            "content": text
        }

    def on_result(self, result):
        item = {
            "url": "cate",
            "content": str(result)
        }
        self.sql.add('newsinfo', **item)
        if not result:
            return
        #print result
        sql_query = "update newsinfo set content=%s where url=%s"
        self.sql.excute(sql_query, (result['url'], result['content']))