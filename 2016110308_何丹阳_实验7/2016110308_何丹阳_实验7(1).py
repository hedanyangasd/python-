from redis import StrictRedis
import pymysql
import requests
import re
from bs4 import BeautifulSoup

#爬取数据
url='https://chengdu.anjuke.com/sale/jinjiang/'

headers={
	'Host':'chengdu.anjuke.com',
	'Refer':'https://chengdu.anjuke.com/sale/jinjiang/',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
	'X-Requested-With':'XMLHttpRequest',
}
# 爬取锦江区二手房的名称、价格、大小、建造年份、联系人、地址、标签。

html=requests.get(url,headers=headers).content.decode('utf-8')

soup = BeautifulSoup(html,'html.parser')

items = soup.find_all(class_='list-item')

redis = StrictRedis(host='localhost',port=6379,db=1,password='')

for i in range(len(items)):
	detail = items[i].find(class_='house-details') 
	pri = items[i].find(class_='pro-price')
	price = pri.find('strong').text
		
	Title = detail.select('a')[0].string.strip() 

	Price = pri.find('strong').text + '万'

	Area = detail.select('span')[1].text
		
	Year = detail.select('span')[3].text
		
	people = detail.select('span')[4].text
	Name = people[1:]

	adds = detail.select('span')[5].text.strip()
	Addre = re.sub('\n| ','',adds)

	tags = detail.find_all(class_='item-tags')
	Tag = ''
	for j in range(len(tags)):
		Tag += tags[j].string + ' '

	#存入redis数据库中
	redis.rpush('item'+str(i+1),'Title:'+Title,'Price:'+Price,'Area:'+Area,'Year:'+Year,'Name:'+Name,'Addre:'+Addre,'Tag:'+Tag)


print("*****存入成功，下面进行各种操作*****")
print("1.获取随机的一个键")
print(redis.randomkey())
print("******************")
print("2.返回键为item1的列表的长度")
print(redis.llen('item1'))
print("******************")
print("3.返回键为item4的列表中1至3之间的元素")
print(redis.lrange('item4',1,3))
print("******************")
print("4.返回键为item3的列表中2位置的元素")
print(redis.lindex('item3',2))
print("******************")
print("5.返回并删除键为item2的列表中的尾元素")
print(redis.rpop('item2'))
print("******************")
print("6.返回并删除键为item5的列表中的首元素")
print(redis.lpop('item5'))
print("******************")
print("7.判断一个键是否存在")
print(redis.exists('item6'))
print("******************")
print("8.判断键类型")
print(redis.type('item7'))
print("******************")
print("9.获取当前数据库中键的数目")
print(redis.dbsize())
