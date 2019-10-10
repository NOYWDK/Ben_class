import os
import csv
import re
from androguard.misc import AnalyzeAPK

def getname(path):
    a, d, x = AnalyzeAPK(path)
    return a.get_app_name()

#使用os.walk(),获得目录下所有文件和文件夹
count=0
list_name = [] #定义一个文件名称列表
list_size = [] #定义一个文件名称列表
fsize=0
dict_file={}

shopping_list=[]
Video_list=[]
news_read_list=[]
social_list=[]
financial_list=[]
game_list=[]
other_list=[]


list_file_tag=[]
list_deal_APK_name=[]

#根据场景预设APK分类标签
shopping_tag=['购','物','商城','淘','MALL','店','买','品','街','折','免税','集','货','优选']
Video_tag=['看片','影音','视频','音乐','直播','TV','歌','体育','播','电视','影视','FM','影院']
news_read_tag=['资讯','阅读','小说','头条','读','书','漫画','日报','新闻','文学']
social_tag=['聊','约','相亲','交友','缘','情感']
financial_tag=['银行','款','付','币','保险','账','金融','贷','钱包','借','钱','证券','理财','财经','股票','财','富','信用','卡']
game_tag=['闯关','捕鱼','英雄','斗地主','大师','枪','棋','牌','疯狂','战','球','赛','麻将','超级','车','跑','冒险','泡泡','游戏','益智','机','逃','竞','绝','换装','驾驶']



#分类
def classify(name):
    flag = 0
    for shoppingtag in shopping_tag:
        if shoppingtag in name:
            if name not in shopping_list:
                shopping_list.append(name)
                list_file_tag.append('shopping')
                flag =1
            else:
                pass
            # Benigan_APK_name.remove(name)
    for Videotag in Video_tag:
        if Videotag in name:
            if name not in Video_list:
                Video_list.append(name)
                list_file_tag.append('video')
                flag =1
            else:
                pass

    for news_readtag in news_read_tag:
        if news_readtag in name:
            if name not in news_read_list:
                news_read_list.append(name)
                list_file_tag.append('news')
                flag =1
            else:
                pass

    for socialtag in social_tag:
        if socialtag in name:
            if name not in social_list:
                social_list.append(name)
                list_file_tag.append('social')
                flag =1
            else:
                pass

    for financialtag in financial_tag:
        if financialtag in name:
            if name not in financial_list:
                financial_list.append(name)
                list_file_tag.append('financial')
                flag =1
            else:
                pass

    for gametag in game_tag:
        if gametag in name:
            if name not in game_list:
                game_list.append(name)
                list_file_tag.append('game')
                flag =1
            else:
                pass
    if(flag == 0):
        list_file_tag.append('other')


path='E:\\MutiSample\\test\\'
for folderName,subfolders,filenames in os.walk(path):
    #打印提示信息
    print('The current folder is '+folderName)
    #打印第一层目录下所有文件和文件夹
    for subfolder in subfolders:
        print('SUBFOLDER OF '+folderName+': '+subfolder)
    #打印第二层目录下的所有文件和文件夹
    for filename in filenames:
        print('FILE INSIDE '+folderName+': '+filename)

        #通过androguard处理文件名，得到应用名称
        try:
            a,d,x=AnalyzeAPK(path+'\\'+filename)
            deal_name=a.get_app_name()
            print("文件名称为" + filename)
            list_name.append(filename)
            print("处理后的APK文件名为"+deal_name)
            list_deal_APK_name.append(a.get_app_name())
            classify(deal_name)
        except:
            print("something wrong with this APK" + filename)
    #每次循环结束打印换行
    # print('')

print("转换后的恶意文件数量为"+str(len(list_deal_APK_name)))



# dict_file=dict(zip(list_name,list_deal_APK_name))

print("-------------------------文件列表分割线---------------------------------")

#写入csv
with open('E:\\MutiSample\\test\\classify.csv','w',encoding='utf-8_sig',newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow([
        'Malicious_APK_name',
        'APK_name',
        'tag',
    ])

    for i in range(0,len(list_deal_APK_name)):
        key = list_name[i]
        values = list_deal_APK_name[i]
        this_tag = list_file_tag[i]
        writeCSV.writerow([key, values, this_tag])






