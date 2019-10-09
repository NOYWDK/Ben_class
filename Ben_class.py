import os
import csv
import re
import shutil #用于拷贝文件

#使用os.walk(),获得目录下所有文件和文件夹
count=0
list_name = [] #定义一个文件名称列表
list_size = [] #定义一个文件名称列表
fsize=0
dict_file={}

shopping_tag=['购','物','商城','淘','MALL','店','买','品','街','折','免税','集','货','优选','超市','market','shop']
Video_tag=['影音','视频','音乐','直播','TV','歌','体育','播放','电视','影视','FM','影院','播','片','video','mp3','player']
news_read_tag=['资讯','阅读','小说','头条','读','书','漫画','日报','新闻','文学']
social_tag=['聊','约','相亲','交友','缘','情感','陌']
financial_tag=['银行','款','付','币','保险','账','金融','贷','钱包','借','钱','证券','理财','财经','股票','财','富','信用','卡']
game_tag=['闯关','捕鱼','英雄','斗地主','极限','枪','西游','棋','牌','疯狂','战','球','赛','麻将','超级','跑','冒险','泡泡','游戏',
          '益智','机','逃亡','竞','绝','换装','驾驶','奥特','星际','拳皇','养成','火柴人','糖果','飞车','射击','大师','欢乐',
          '连连看','块','3D','大富翁','扑克']


Benigan_APK_name=[]
index_list=[] #符合标签的APK索引列表
other_index_list=[] #其他类APK索引列表
Benigan_index_list= range(0, 19069) #Benigan索引列表，即0-19068


shopping_list=[]
Video_list=[]
news_read_list=[]
social_list=[]
financial_list=[]
game_list=[]
other_list=[]


#读取Benigan_APK名称
filename='Benigan_APK_name.csv'
with open(filename,encoding='utf-8_sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Benigan_APK_name.append(row['Benigan_APK_name'])
for name in Benigan_APK_name:
    for shoppingtag in shopping_tag:
        if shoppingtag in name:
            if name not in shopping_list:
                shopping_list.append(name)
                Ben_index = Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)
    for Videotag in Video_tag:
        if Videotag in name:
            if name not in Video_list:
                Video_list.append(name)
                Ben_index=Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)
    for news_readtag in news_read_tag:
        if news_readtag in name:
            if name not in news_read_list:
                news_read_list.append(name)
                Ben_index=Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)
    for socialtag in social_tag:
        if socialtag in name:
            if name not in social_list:
                social_list.append(name)
                Ben_index=Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)
    for financialtag in financial_tag:
        if financialtag in name:
            if name not in financial_list:
                financial_list.append(name)
                Ben_index=Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)
    for gametag in game_tag:
        if gametag in name:
            if name not in game_list:
                game_list.append(name)
                Ben_index=Benigan_APK_name.index(name)
                index_list.append(Ben_index)
            else:
                pass
            # Benigan_APK_name.remove(name)

def copyAPK(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        # fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        # if not os.path.exists(fpath):
        #     os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

def moveAPK(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        # fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        # if not os.path.exists(fpath):
        #     os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

#查找所有未被打标签的APK位置
for item in Benigan_index_list:
    if item not in index_list:
        other_index_list.append(item)

for position in other_index_list:
    other_list.append(Benigan_APK_name[position])

#移动文件
for shoppingfile in shopping_list:
    src_shopping_file = 'G:\\BeniganAPK\\' + shoppingfile
    dst_shopping_file = 'G:\\BeniganAPK\\shopping\\'+shoppingfile
    moveAPK(src_shopping_file, dst_shopping_file)

for videofile in Video_list:
    src_Video_file = 'G:\\BeniganAPK\\' + videofile
    dst_Video_file = 'G:\\BeniganAPK\\video\\'+videofile
    moveAPK(src_Video_file, dst_Video_file)

for readfile in news_read_list:
    src_read_file = 'G:\\BeniganAPK\\' + readfile
    dst_read_file = 'G:\\BeniganAPK\\read\\'+readfile
    moveAPK(src_read_file, dst_read_file)

for socialfile in social_list:
    src_social_file = 'G:\\BeniganAPK\\' + socialfile
    dst_social_file = 'G:\\BeniganAPK\\social\\'+socialfile
    moveAPK(src_social_file, dst_social_file)

for financiallfile in financial_list:
    src_financiall_file = 'G:\\BeniganAPK\\' + financiallfile
    dst_financiall_file = 'G:\\BeniganAPK\\financial\\'+financiallfile
    moveAPK(src_financiall_file, dst_financiall_file)

for gamefile in game_list:
    src_game_file = 'G:\\BeniganAPK\\' + gamefile
    dst_game_file = 'G:\\BeniganAPK\\game\\'+gamefile
    moveAPK(src_game_file, dst_game_file)

for otherfile in other_list:
    src_other_file = 'G:\\BeniganAPK\\' + otherfile
    dst_other_file='G:\\BeniganAPK\\other\\'+otherfile
    moveAPK(src_other_file, dst_other_file)


print(Benigan_APK_name)
print("购物类APK如下：",shopping_list)
print("购物类APK数量总共：",str(len(shopping_list)))

print("影音类APK如下：",Video_list)
print("影音类APK数量总共：",str(len(Video_list)))

print("阅读类APK如下：",news_read_list)
print("阅读类APK数量总共：",str(len(news_read_list)))

print("社交类APK如下：",social_list)
print("社交类APK数量总共：",str(len(social_list)))

print("理财类APK如下：",financial_list)
print("理财类APK数量总共：",str(len(financial_list)))

print("游戏类APK如下：",game_list)
print("游戏类APK数量总共：",str(len(game_list)))

print("其他类APK如下：",other_list)
print("其他类APK数量总共：",str(len(other_list)))