from pyquery import PyQuery as pq

f = pq("http://www.chinadaily.com.cn/business/2016-09/22/content_26859929.htm")

item = f("div.pt30")
print item


text = ""
for each in item('p').items():
    text = text + each.text() + '\n'

print text
