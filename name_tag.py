import os
import csv

APK_name = []
list_file_tag = []

shopping_list=[]
Video_list=[]
news_read_list=[]
social_list=[]
financial_list=[]
game_list=[]
other_list=[]

all_list = []

#根据场景预设APK分类标签
shopping_tag=['购','省','商','淘','MALL','店','买','品','街','折','免税','集市','货','选','購物','珠宝','饮','单','利','AirPay','Store','百貨','享','超市','咸鱼','美团','特价','网','Shop']
Video_tag=['StudioKA','看片','影音','视','音乐','直播','TV','歌','体育','播','电视','影视','FM','影院','拍','摄影','影集','铃','咪咕','ELive','Video','Videos','Photo','Player','DJ','相册','看看']
news_read_tag=['News','资讯','阅读','小说','头条','读','书','漫画','日报','新闻','嗅','文学','题','文字','学','拾集','宝典','英语','趣看','词典','全集']
social_tag=['聊','约会','相亲','交友','缘','情感','职','恋','社交','掌上','旅','校','合伙','云','邦','聚会','圈','城','汇','生活','社区','飞信']
financial_tag=['签约','银行','款','付','币','保险','账','金融','贷','钱包','借','钱','证券','理财','财经','股','财','富','信用','卡','社保','红包','赢','券','票','赚','房信','税','链']
game_tag=['闯关','捕鱼','英雄','斗地主','大师','消消乐','枪','棋','牌','疯狂','战','球','赛','麻将','超级','车','跑','冒险','泡泡','游戏','益智','抓娃娃','机','逃','竞','绝','换装','驾驶','农场','吃鸡','乐园','弹','王者','飞','填','走','切','躲','瓜','乱斗','开','踩','找茬','涂','战','武','侠']

def readCSV():
    path ='E:\\Ben_class\\allsample.csv'  #黑
    with open(path,encoding='gbk')as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            APK_name.append(row['APK_name'])

#分类
def classify(name):
    flag =0
    for shoppingtag in shopping_tag:
        if shoppingtag in name:
            if name not in shopping_list:
                tup = (name, 'shopping')
                all_list.append(tup)
        # shopping_list.append(name)
        # list_file_tag.append('shopping')
                flag =1
                return
        else:
            pass

    for Videotag in Video_tag:
        if Videotag in name:
            if name not in Video_list:
                tup = (name, 'video')
                all_list.append(tup)
            # Video_list.append(name)
            # list_file_tag.append('video')
                flag =1
                return
        else:
            pass

    for news_readtag in news_read_tag:
        if news_readtag in name:
            if name not in news_read_list:
                tup = (name, 'news')
                all_list.append(tup)
            # news_read_list.append(name)
            # list_file_tag.append('news')
                flag =1
                return
        else:
            pass

    for socialtag in social_tag:
        if socialtag in name:
            if name not in social_list:
                tup = (name, 'social')
                all_list.append(tup)
            # social_list.append(name)
            # list_file_tag.append('social')
                flag =1
                return
        else:
            pass

    for financialtag in financial_tag:
        if financialtag in name:
            if name not in financial_list:
                tup = (name, 'financial')
                all_list.append(tup)
            # financial_list.append(name)
            # list_file_tag.append('financial')
                flag =1
                return
        else:
            pass

    for gametag in game_tag:
        if gametag in name:
            if name not in game_list:
                tup = (name, 'game')
                all_list.append(tup)
            # game_list.append(name)
            # list_file_tag.append('game')
                flag =1
                return
        else:
            pass

    if(flag ==0):
        tup = (name, 'other')
        all_list.append(tup)
        # all_list.append('other')
        return

readCSV()
for name in APK_name:
    classify(name)

print("-------------------------文件列表分割线---------------------------------")

#写入csv
with open('E:\\Ben_class\\classify_all.csv','w',encoding='utf-8_sig',newline='')as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow([
        'APK_name',
        'tag',
    ])

    for i in range(0,len(all_list)):
        apk_name = all_list[i][0]
        this_tag = all_list[i][1]
        writeCSV.writerow([ apk_name, this_tag])
        print('文件名：' + apk_name +'类：' + this_tag)
