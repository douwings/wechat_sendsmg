# -*- coding: utf-8 -*-
import itchat
import time

print('scanQR')
itchat.auto_login(hotReload=True)

boom_remark_name = input('input name:  ')

message = input('input msg:  ')

boom_obj = itchat.search_friends(remarkName=boom_remark_name)[0]['UserName']
while True:
    time.sleep(0.5)
    print('doing...')
    itchat.send_msg(msg=message, toUserName=boom_obj)
    path = 'C:\\Users\\Administrator\\Desktop\\py\\img\\image\\timg (2).jpg'
    itchat.send_image(fileDir=path, toUserName=boom_obj)
