import re
import requests
import csv
from urllib.parse import urlencode

base_url='http://m.weibo.cn/api/container/getIndex?'
headers={
	'Host':'m.weibo.cn',
	'Refer':'https://m.weibo.cn/u/1739046981?uid=1739046981&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%9D%8E%E8%8D%A3%E6%B5%A9',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
	'X-Requested-With':'XMLHttpRequest',
}

def get_page(page):
	params={
		'type':'uid',
		'value':'1739046981',
		'containerid':'1076031739046981',
		'page':page,
	}
	url=base_url+urlencode(params)
	response=requests.get(url,headers=headers)
	if response.status_code == 200:
		return response.json()


dic = []
for i in range(1,10):
	json = get_page(i)
	cards = json['data']['cards']
	for j in range(len(cards)):
		mblog = cards[j].get('mblog')
		if mblog == None:
			continue
		created_at = mblog['created_at']
		reposts_count = mblog['reposts_count']
		comments_count = mblog['comments_count']
		attitudes_count = mblog['attitudes_count']
		text = mblog['text']
		Text = re.sub('<.*?>','',text)
		info = {'时间':created_at,'转发数':reposts_count,'评论数':comments_count,'点赞数':attitudes_count,'内容':Text}
		dic.append(info)
		print('************************')
		print('时间: '+created_at)
		print(f'转发: {reposts_count}')
		print(f'评论: {comments_count}')
		print(f'点赞: {attitudes_count}')
		print('text: '+Text)


with open('2016110308_何丹阳_实验4_1.csv',"w",newline="",encoding='utf-8-sig') as f:
	writer = csv.DictWriter(f, fieldnames=['时间','转发数','评论数','点赞数','内容'])
	writer.writeheader()
	writer.writerows(dic)


