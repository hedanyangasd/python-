# -*- coding: utf-8 -*-
#找出一串字符中某个字母出现第二次或者第三次的位置

strings = input('请输入字符串\n')
ch = input('请输入要查找的字符\n')

second = strings.find(ch,strings.find(ch)+1)

third = strings.find(ch,strings.find(ch,strings.find(ch)+1)+1)

print ('该字符出现第二次的位置是：' + str(second) )
print ('该字符出现第三次的位置是：' + str(third) )
