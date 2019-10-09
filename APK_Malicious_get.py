import os
import csv
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
list_mutis=['expense','fraud','others','payment','privacy','remote','rogue','spread','system']
list_mutis_1=['expense']
list_mutis_2=['payment']
list_mutis_3=['fraud','others','privacy','spread','system']
list_mutis_4=['remote','rogue']


list_file_tag=[]
list_deal_APK_name=[]

#根据场景预设APK分类标签
shopping_tag=['购','物','商城','淘','MALL','店','买','品','街','折','免税','集','货','优选']
Video_tag=['影音','视频','音乐','直播','TV','歌','体育','播放','电视','影视','FM','影院']
news_read_tag=['资讯','阅读','小说','头条','读','书','漫画','日报','新闻','文学']
social_tag=['聊','约','相亲','交友','缘','情感']
financial_tag=['银行','款','付','币','保险','账','金融','贷','钱包','借','钱','证券','理财','财经','股票','财','富','信用','卡']
game_tag=['闯关','捕鱼','英雄','斗地主','大师','枪','棋','牌','疯狂','战','球','赛','麻将','超级','车','跑','冒险','泡泡','游戏','益智','机','逃亡','竞','绝','换装','驾驶']

for list_muti in list_mutis:
    path='G:\\MutiSample\\'+list_muti
    for folderName,subfolders,filenames in os.walk(path):
        #打印提示信息
        print('The current folder is '+folderName)
        #打印第一层目录下所有文件和文件夹
        for subfolder in subfolders:
            print('SUBFOLDER OF '+folderName+': '+subfolder)
        #打印第二层目录下的所有文件和文件夹
        for filename in filenames:
            print('FILE INSIDE '+folderName+': '+filename)

            # cut_line=filename.find('_') #根据下划线截取病毒名称
            # start_line_num=cut_line+1
            #
            # vir_name=filename[start_line_num:]
            #通过androguard处理文件名，得到应用名称
            try:
                a,d,x=AnalyzeAPK(path+'\\'+filename)
                deal_name=a.get_app_name()
                print("文件名称为" + filename)
                list_name.append(filename)
                print("处理后的APK文件名为"+deal_name)
                list_deal_APK_name.append(a.get_app_name())
            except:
                print("something wrong with this APK" + filename)
            #获得文件的大小
            # fsize = os.path.getsize('G:\\MutiSample\\'+list_muti+'\\'+filename)
            # fsize = fsize / float(1024 * 1024)
            # filesize=round(fsize, 2)
            # print("文件大小为" + str(filesize)+'MB')
            # list_size.append(filesize)

            count=count+1
            list_file_tag.append(list_muti)
        #每次循环结束打印换行
        print('')
print("一共"+str(count)+"个文件")
print("转换后的恶意文件数量为"+str(len(list_deal_APK_name)))



dict_file=dict(zip(list_name,list_deal_APK_name))

print("-------------------------文件列表分割线---------------------------------")

#写入csv
with open('G:\\MutiSample\\Malicious_APK_name.csv','w',encoding='utf-8_sig',newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow([
        'Malicious_APK_name',
        'APK_name',
        'tag',
    ])
    for this_tag in list_file_tag:
        for key, values in dict_file.items():
            writeCSV.writerow([key, values, this_tag])