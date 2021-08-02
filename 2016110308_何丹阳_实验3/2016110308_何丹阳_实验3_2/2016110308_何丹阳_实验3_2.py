import lxml.html
import requests
import csv
import re

url = "https://cd.58.com/danche/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_LOGO&PGTID=0d100000-0006-65cf-8c8e-dfd8022dc585&ClickID=31"
html1 = requests.get(url).content.decode()
html2 = re.sub('\r\n\t\t\t\t\t\t\t','',html1)
html3 = re.sub('\t\t','',html2)
html4 = re.sub('\r\n    \t','',html3)
html5 = re.sub('\t','',html4)
html = re.sub('\r\n\t\t    \t\t\t','',html5)

selector = lxml.html.fromstring(html)

#获取题目
name_list = selector.xpath('//td[@class="t"]/a/text()')

#获取内容
content_list = selector.xpath('//div[@class="item-desc"]/text()')

#获取地址
add_list = selector.xpath('//a[@class="c_666"][1]/text()')

#获取url
url_list = selector.xpath('//td[@class="t"]/a/@href')

#获取价格
price_list = selector.xpath('//b[@class="pri"]/text()')

#字典
dic = []

for i in range(3,len(name_list)):
	info = {'标题':name_list[i],'内容':content_list[i],'地址':add_list[i],'链接':url_list[i],'价格':price_list[i]}
	dic.append(info)

with open('2016110308_何丹阳_实验3_2.csv',"w",newline="",encoding='utf-8-sig') as f:
	writer = csv.DictWriter(f, fieldnames=['标题','内容','地址','链接','价格'])
	writer.writeheader()
	writer.writerows(dic)




