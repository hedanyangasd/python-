import re
import requests
import os
from multiprocessing.dummy import Pool


#新建文件夹函数
def mkdir(path):
	folder = os.path.exists(path)
	if not folder:
		os.makedirs(path)
		print("Ok")
	else:
		print("the file is exit")


#爬取内容存入文件夹里
def query(url):
	url1 = "https://www.kanunu8.com/book3/6879/"
	chapter = requests.get(url1+url).content.decode('GBK')
	title1 = re.search(' (.*?)_动物庄园',chapter).group()
	Title = re.sub(" ","",title1)
	content = re.findall('<[pbr /]{1,5}>\r\n\u3000\u3000(.*?)<',chapter)
	filename = file+'\\'+Title+'.txt'
	print(filename)
	with open(filename, 'w', encoding='utf-8') as f:
		for i in range(0,len(content)):
			f.write(content[i])
			f.write('\n')

	
#创建文件夹
file = '动物庄园'
mkdir(file)

url = "https://www.kanunu8.com/book3/6879/"
html = requests.get(url).content.decode('GBK')

list1 = re.findall('<td width="25%"><a href="(.*?)">',html)
list2 = re.findall('<td><a href="(.*?)">',html)
url_list = list1+list2
print(url_list)

#多线程
pool = Pool(4)
pool.map(query,url_list)
print("爬虫完成")


