import requests
import re
f = open('2016110308_何丹阳_实验2.txt','r+',encoding='utf-8')
htmls = f.read()
f.close()


sub = re.sub('<img.*?/>',"",htmls)
name = re.findall('fr=pb>" target="_blank">(.*?)</a>',sub)
date = re.findall('<span class="tail-info">(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2})</span>',htmls)

content = re.findall('<div id="post_content.*?>            (.*?)<',htmls)

for i in range(len(name)):
	print(f'name:{name[i]}')
	print(f'date:{date[i]}')
	print(f'content:{content[i]}')
	print(f'**************')
