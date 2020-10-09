import os, re, sys
import platform
from os.path import exists
from functions_process import find_num_bus
from functions_preparation import JavFile
from functions_dbcheck import pure_check_if_ID_exist
import pandas as pd
from pandas import DataFrame
import numpy as np
#read txt row seperated by first and last comma

def read_to_db(txt_file):
    my_file = open(txt_file, encoding="utf-8")
    arr=np.array([]).reshape(0,3)
    for k in my_file.readlines():
        # print (k)
        string1=str(k.split(",")[0])
        len1=len(string1)
        string3=str(k.split(",")[-1])
        len3=len(string3)
        stringfull=str(k)
        fulllen=len(stringfull)
        posstart=len1+1
        posend=fulllen-1-len3
        string2=str(k)[posstart:posend]
        rowtext=[string1,string2,string3]
        # print (k.split(","))
        # print(k.split(",")[1])
        # print(k.split(",")[-2])
        # text = [k.split(",")[0]]+[''.join(k.split(",")[1:-2])]+[k.split(",")[-1]] 
        newarr=np.array(rowtext)
        arr=np.vstack((arr,newarr))
    text=arr
    my_file.close()
    df= pd.DataFrame(text)
    # next line is optional, just if you want named columns
    df.columns = ['file_ID','file_path','size']
    # print(df)
    return df


# get folder size
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

# Convert bytes to KB, MB, GB, TB
def format_bytes(size):
# 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return round(size,2), power_labels[n]

#create level one folder name list
def list_creation(path):
    try:
        scope= next(os.walk(path))[1]
        return scope
    except StopIteration:
        pass

# move_folder
def move_folder(old_folder_path, new_folder_path):
    if(old_folder_path!=new_folder_path) and (not exists(new_folder_path)):
        os.rename(old_folder_path, new_folder_path)
        print(old_folder_path +" is removed to "+ new_folder_path)
        return True
    else:
        print("Error: will try to move"+ old_folder_path +"  to folder remove1")
        return False
           
def same_list_creation(c,d):
    same_folder_list=[]
    a=list_creation(c)
    b=list_creation(d)
    same_folder_list=list(set(a).intersection(b))
    return same_folder_list


def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


#  switch between abbreviation folder
def process_folder(path,sub_folder_name):

    #path="G:\My Drive\Video\Torrent_F\有码"
    path+=sub_folder_name  

    # count=0
    # i='ABP'
    for i in list_creation(path):
        # sub_folder_path="G:\My Drive\Video\Torrent_F\有码\ABP"
        sub_folder_path=os.path.join(path, i)
        for j in list_creation(sub_folder_path):
            # sub_folder_path2="G:\My Drive\Video\Torrent_F\有码\ABP\ABP-001"
            sub_folder_path2=os.path.join(sub_folder_path, j)
            size=get_size(sub_folder_path2)
             #cdate=creation_date(sub_folder_path)
            # count+=1
            print(j,',',size,sep='') #remove wtite spaces around variables



# db generation for my drive and migration shared drive
def db_csv_generation():
    f=open('E:\VS Projects\Vscode\javsdt\GlobalScan.csv', 'w')
    sys.stdout = f
    print( 'ID,Size') #print the label on the table
    sub_folder_name=['有码','素人']
    path=["G:\My Drive\Video\Torrent_F\\","G:\Shared drives\Migration\Torrent_F\\"]
    for pathname in path:
        for foldername in sub_folder_name:
            process_folder(pathname,foldername)
    f.close()

# Function: scan other shared drive to get the ID list
def scan_path(root_choose,csv_name,skipList):
    # 初始化 当前系统的路径分隔符 windows是“\”，linux和mac是“/”
    sep = os.sep
    custom_file_type = "MP4、MKV、AVI、WMV、ISO、RMVB、FLV、TS、RM"
    custom_surplus_words="XHD1080、MM616、FHD-1080、BIG-2048、big2048、FENGNIAO、nyap2p.com、UUE29、UUF39、UUF87、UUP87、UUW62、UUS75、UUV97、VIP1196、A57X、QQ视频、IMG-、VID-20、x264、BeautyBox_20、TS_、hlq8712"
    custom_suren_pref="BMH、BNJC、CUTE、DCV、EMOI、EVA、EWDX、EXMU、EZD、FAD、FCTD、GANA、GAREA、GAV、GERBM、GERK、HEN、HMDN、HOI、HSAM、HYPN、IMDK、INST、ION、\
        JAC、JKK、JKZ、JOTK、KAGD、KJN、KNB、KSKO、KURO、LADY、LAFBD、LAS、LUXU、MAAN、MGDN、MISM、MIUM、MMGH、MMH、MNTJ、MTP、MY、NAMA、NNPJ、NTK、NTTR、OBUT、\
        ORE、OREBMS、OREC、OREP、ORERB、ORETD、ORETDP、OREX、OTIM、PAPA、PER、PKJD、REP、SCP、SCUTE、SHOW、SHYN、SIMM、SIRO、SPOR、SPRM、SQB、SRCN、SRHO、SRTD、SSAN、STKO、SUKE、SVMM、SWEET、SYBI、URF、VOV、YKMC"
    tuple_type = tuple(custom_file_type.split('、'))        # 需要扫描的文件的类型
    list_surplus_words = custom_surplus_words.split('、')
    list_suren_num = custom_suren_pref.split('、') 
    file_path_name='E:\VS Projects\Vscode\javsdt\\'+csv_name+'.csv'
    table_name="DISTINCTID"
    #sys.stdout = open(file_path_name, 'w')
    fp=open(file_path_name, 'w', encoding='utf-8')
    for root, dirs, files in os.walk(root_choose):
        if not files:
            continue
        # 对这一层文件夹进行评估,有多少视频，有多少同车牌视频，是不是独立文件夹

        list_jav_videos = []         # 存放：需要整理的jav的结构体
        dict_car_pref = {}           # 存放：这一层文件夹下的几个车牌 abp avop snis。。。{'abp': 1, avop': 2} abp只有一集，avop有cd1、cd2
        num_videos_include = 0       # 当前文件夹中视频的数量，可能有视频不是jav
        dict_subt_files = {}         # 存放：jav的字幕文件 {'c:\a\abc_123.srt': 'abc-123'}
        # 判断文件是不是视频，放入list_jav_videos中
        for file_raw in files:
            file_temp = file_raw.upper()
            if file_temp.endswith(tuple_type) and not file_temp.startswith('.'):
                num_videos_include += 1
                for word in list_surplus_words:
                    file_temp = file_temp.replace(word, '')
                # jav_num 视频中的车牌
                jav_num = find_num_bus(file_temp, list_suren_num)
                if jav_num:
                    try:
                        dict_car_pref[jav_num] += 1  # 已经有这个车牌了，加一集cd
                    except KeyError:
                        dict_car_pref[jav_num] = 1  # 这个新车牌有了第一集
                    # 把这个jav的各种属性打包好
                    jav_struct = JavFile()
                    jav_struct.num = jav_num           # 车牌
                    jav_struct.file = file_raw         # 原文件名
                    jav_struct.episodes = dict_car_pref[jav_num]  # 当前jav，是第几集  {'abp': 1, avop': 2}
                    # 这个车牌在dict_subt_files中，有它的字幕。
                    if jav_num in dict_subt_files.values():
                        jav_struct.subt = list(dict_subt_files.keys())[list(dict_subt_files.values()).index(jav_num)]
                        del dict_subt_files[jav_struct.subt]
                    list_jav_videos.append(jav_struct)
                #else:
                    #print('>>无法处理：' + root.replace(root_choose, '') + sep + file_raw)
        # 正式开始
        # print(list_jav_videos)
        for jav in list_jav_videos:
            jav_raw_num = jav.num  # 车牌  abc-123
            jav_already_have= pure_check_if_ID_exist(jav_raw_num,table_name)
            if not jav_already_have:
                #check the front id we already collect
                if pure_check_if_Front_ID_collect(jav_raw_num,Full_ID_List()):
                    if not pure_check_if_want_to_skip(jav_raw_num,skipList):
                        jav_file = jav.file    # 完整的原文件名  abc-123.mp4
                        jav_epi = jav.episodes  # 这是第几集？一般都只有一集
                        num_all_episodes = dict_car_pref[jav_raw_num]  # 该车牌总共多少集
                        path_jav = root + sep + jav_file
                        # record_content_without_path=jav_raw_num+','+ jav_file+','+str(jav_already_have)+','+str(jav_epi)+ '/' +str(num_all_episodes)
                        record_content_without_path=jav_raw_num+','+ jav_file+','+str(jav_epi)+ '/' +str(num_all_episodes)
                        record_content=record_content_without_path+','+path_jav
                        str_content = record_content.encode().decode('utf-8')
                        fp.write(str_content)
                        fp.write("\n")
                        print(record_content_without_path)
    fp.close() 

#combine two list with order
def combine_List(L1,L2):
    set1=set(L1)
    set2=set(L2)
    set_union=set1.union(set2)
    result=sorted(set_union)
    return result

#list all combination
def Full_ID_List():
    sub_folder_name=['有码','素人']
    path=["G:\My Drive\Video\Torrent_F\\","G:\Shared drives\Migration\Torrent_F\\"]
    
    List=[]
    for pathname in path:
        for foldername in sub_folder_name:
            path=pathname+foldername
            List=combine_List(list_creation(path),List)
    return List

#check if we collect this front id
def pure_check_if_Front_ID_collect(jav_raw_num,List):
    front_id=jav_raw_num.split('-')[0]
    if front_id in List:
        return True
    else:
        return False

def pure_check_if_want_to_skip(jav_raw_num,List):
    front_id=jav_raw_num.split('-')[0]
    if front_id in List:
        return True
    else:
        return False