import requests
import re
import csv
from bs4 import BeautifulSoup


url='https://chengdu.anjuke.com/sale/jinjiang/'

headers={
	'Host':'chengdu.anjuke.com',
	'Refer':'https://chengdu.anjuke.com/sale/jinjiang/',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
	'X-Requested-With':'XMLHttpRequest',
}
# 爬取锦江区价格在150-200万以内的二手房的名称、价格、大小、建造年份、联系人、地址、标签。

html=requests.get(url,headers=headers).content.decode('utf-8')

soup = BeautifulSoup(html,'html.parser')

items = soup.find_all(class_='list-item')

dic = []
for i in range(len(items)):
	detail = items[i].find(class_='house-details') 
	pri = items[i].find(class_='pro-price')
	price = pri.find('strong').text
	if float(price) < 200 and float(price) > 150:
		print('********************************************')
		Title = detail.select('a')[0].string.strip()
		print(Title)

		Price = pri.find('strong').text + '万'
		print(Price)

		Area = detail.select('span')[1].text
		print(Area)

		Year = detail.select('span')[3].text
		print(Year)

		people = detail.select('span')[4].text
		Name = people[1:]
		print(Name)

		adds = detail.select('span')[5].text.strip()
		Addre = re.sub('\n| ','',adds)
		print(Addre)

		tags = detail.find_all(class_='item-tags')
		Tag = ''
		for i in range(len(tags)):
			Tag += tags[i].string + ' '
		print(Tag)
		info = {'名称':Title,'价格':Price,'大小':Area,'建造年份':Year,'联系人':Name,'地址':Addre,'标签':Tag}
		dic.append(info)



with open('2016110308_何丹阳_实验4_2.csv',"w",newline="",encoding='utf-8-sig') as f:
	writer = csv.DictWriter(f, fieldnames=['名称','价格','大小','建造年份','联系人','地址','标签'])
	writer.writeheader()
	writer.writerows(dic)

