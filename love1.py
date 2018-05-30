from __future__ import unicode_literals

from threading import Timer

from wxpy import  *

import requests

bot = Bot()

# bot = Bot(console_qr=2, cache_path='botoo.pkl') #这里的二维码是用像素的形式打印出来！，如果你在win环境上运行，替换为bot=Bot()

def get_news1():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation

def test():
    print(get_news1()[0])
    print(len(get_news1()))
    # print(len(get_news1()))
    print(get_news1()[1])
    str = "现在征集每日投稿"
    print(str.index("征集每日"))
    print(str[0:5])

def send_news():
    try:
        my_friend = bot.friends().search(u"赛博")[0]    # 你朋友的微信昵称，不是备注，也不是微信帐号。
        my_friend.send(get_news1()[0])        # 此处获取的是get_news1()方法返回列表的第一部分内容
        pos = get_news1()[1].index("现征集每日一句投稿")
        message = ""
        my_friend.send(get_news1()[1][5:pos])     #词霸小编：野草遮不住太阳的光芒，……，即去掉词霸小编：
        i = 0
        while i < 100:
            my_friend.send("第" + str(i)  + "次"+ "表白" + u" l love you")
            i = i + 1
        t = Timer(86400, send_news)     # 每86400秒（1天），发送1次，不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，很麻烦的一件事，就让他一直挂着吧
        t.start()

    except:
        my_friend = bot.friends().search("悲观的乐天派")[0]  # 你的微信昵称，不是微信帐号。
        my_friend.send(u"宕机了，请公司帮忙查一下故障，今天消息发送失败了 + msg: wrong")

if __name__ == "__main__":
    send_news()

