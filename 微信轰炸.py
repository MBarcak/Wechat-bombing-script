import itchat
import time

def SendToGroup():
    group = input('输入要轰炸的群聊:')

    try:
        my_group = itchat.search_chatrooms(name = group)[0]['UserName']
    except:
        print("未找到群聊！")
        return None
    num = int(input('输入轰炸的次数:'))
    b = str(input('输入要轰炸的内容:'))
    num_time = float(input('输入轰炸间隔:'))
    
    i = 0

    itchat.send('您的好友正在轰炸',toUserName = my_group)
    while i != num:
        itchat.send(b,toUserName = my_group)
        time.sleep(num_time)
        i += 1

    itchat.send('轰炸完毕',toUserName = my_group)
    print("轰炸完毕！")



def SendToFriend():
    friend = input('输入要轰炸的好友:')

    try:
        my_friend = itchat.search_friends(name = friend)[0]['UserName']
    except:
        print("未找到用户！")
        return None
    
    num = int(input('输入轰炸的次数:'))
    b = str(input('输入要轰炸的内容:'))
    num_time = float(input('输入轰炸间隔:'))
    
    i = 0

    itchat.send('您的好友正在轰炸',toUserName = my_friend)
    while i != num:
        itchat.send(b,toUserName = my_friend)
        time.sleep(num_time)
        i += 1

    itchat.send('轰炸完毕',toUserName = my_friend)
    print("轰炸完毕！")
        
itchat.auto_login(hotReload=True)

while True:
    mode = int(input('选择你要轰炸的模式(个人输入1，群聊输入2，退出输入0):'))

    if mode == 1:
        SendToFriend()
    elif mode == 2:
        SendToGroup()
    elif mode == 0:
        break
    else:
        print("输入错误，请重新输入！")

itchat.logout()
