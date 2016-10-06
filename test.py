from pyquery import PyQuery as pq
import MySQLdb as mdb


f = pq("http://www.chinadaily.com.cn/business/money_21.html")
news = list()
for item in f("div.busBox1").items():
    info = dict()
    info["name"] = item("a[href$='.htm']").text()
    info["url"] = "http://www.chinadaily.com.cn/business/"+item("a[href$='.htm']").attr.href
    info["time"] = ""
    info["content"] = item("p")
    news.append(info)

print news