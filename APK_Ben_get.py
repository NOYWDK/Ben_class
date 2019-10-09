import os
import csv
#使用os.walk(),获得目录下所有文件和文件夹
count=0
list_name = [] #定义一个文件名称列表
list_size = [] #定义一个文件名称列表
fsize=0
dict_file={}


for folderName,subfolders,filenames in os.walk('G:\\BeniganAPK'):
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
        print("文件名称为"+filename)
        list_name.append(filename)
        fsize = os.path.getsize('G:\\BeniganAPK\\'+filename)
        fsize = fsize / float(1024 * 1024)
        filesize=round(fsize, 2)
        print("文件大小为" + str(filesize)+'MB')
        list_size.append(filesize)
        count=count+1

    #每次循环结束打印换行
    print('')
print("一共"+str(count)+"个文件")
print(list)


dict_file=dict(zip(list_name,list_size))

print("-------------------------文件列表分割线---------------------------------")

#写入csv
with open('Benigan_APK_name.csv','w',encoding='utf-8_sig',newline='') as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow([
        'Benigan_APK_name',
        'filesize(MB)',
    ])
    for key, values in dict_file.items():
        writeCSV.writerow([key, values])
