from selenium import webdriver
import pymysql
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Firefox(executable_path=r"geckodriver.exe")
url= 'http://book.zongheng.com/store.html'
dic = []

try:
	browser.get(url)
except TimeoutException:
	print("Time out")

try:
	bookinfo = browser.find_elements_by_class_name('bookinfo')
	for i in bookinfo:
		bookname = i.find_elements_by_class_name('bookname')
		for j in bookname:
			name = j.text

		bookilnk = i.find_elements_by_class_name('bookilnk')
		for j in bookilnk:
			infoma = j.text.split('| ')
			author = infoma[0]
			novel_type = infoma[1]
			load = infoma[2]
			update = infoma[3]

		info = {'name':name,'author':author,'classful':novel_type,'status':load,'uptime':update}
		dic.append(info)

except NoSuchElementException:
	print("No Element")

finally:
	browser.close()
	print("执行完成！")



db = pymysql.connect(host='localhost',user='root',password='root',port=3306)
cursor = db.cursor()

sql1 = "DROP DATABASE IF EXISTS hedanyang"
cursor.execute(sql1)
sql2 = "CREATE DATABASE hedanyang  DEFAULT CHARACTER SET utf8"
cursor.execute(sql2)
sql3 = "USE hedanyang"
cursor.execute(sql3)

sql4="CREATE TABLE IF NOT EXISTS noval(\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `name` varchar(200)  NOT NULL,\
  `author` varchar(200) NOT NULL,\
  `classful` varchar(100) NOT NULL,\
  `status` varchar(100) NOT NULL,\
  `uptime` varchar(200) NOT NULL,\
  PRIMARY KEY (`id`))"
cursor.execute(sql4)

for i in range(0,len(dic)):
	data = dic[i]
	print(data)
	table = 'noval'
	keys=','.join(data.keys())
	print(data.keys())
	values=','.join(['%s']*len(data))
	print(values)
	print(data.values())
	sql5 = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)

	try:
	    if cursor.execute(sql5,tuple(data.values())):
	        db.commit()
	        print("添加成功")
	except:
	    db.rollback()
	    print("添加失败")
    
db.close()