# To compare size of folders and remove the smaller video ACROSS DIFFERENT GOOGLE DRIVE for Suren and Youma
#Fully Auto

#########Fix
# adding the wuma and FC2:checked
# fix the counting issue by reference list:checked
# seperate the level1 and level2 folder process functions:checked
# change path premeters to make it easy to call for rclone to mount:checked
# need to fix the name to long that it cannot find the path
# need to fix the one level down files check ...

import os, re, sys
from os.path import exists
from re import findall
from re import search
from configparser import RawConfigParser
from shutil import copyfile
from traceback import format_exc
from tkinter import filedialog, Tk

from functions_scan import get_size, format_bytes, list_creation, move_folder,same_list_creation,file_list_compare

sep = os.sep
sys.stdout = open('log/CompareList.txt', 'w')

root_mydrive="G:\\My Drive\\"
root_migration="G:\\Shared drives\\Migration\\"

# root_mydrive="Y:\\"
# root_migration="Z:\\"

root_to_remove=root_migration+"To remove"
root_to_remove1=root_to_remove+"1"  #To remove1


def level1_folder_to_Process(root_choose2,root_to_compare2,root_to_remove,root_to_remove1,count):
    for i in same_list_creation(root_choose2,root_to_compare2):
        folder_path_a=os.path.join(root_choose2, i)
        folder_path_b=os.path.join(root_to_compare2, i)
        size_a=get_size(folder_path_a) 
        size_b=get_size(folder_path_b) 
        new_folder_path=os.path.join(root_to_remove,i) 
        new_folder_path1=os.path.join(root_to_remove1,i) 
        count[0]+=1 #variable reference assignment

        # if 1.01*size_a>size_b:
        #if size_a>=size_b:
        size_delta=size_a-size_b
        # if size_delta>=0 and size_delta<=300:
        # if size_delta>=0 and size_delta<=800000:
        mark=file_list_compare(folder_path_a,folder_path_b)
        if size_delta>=0:
            if mark[0]:
                str_content = str(mark[1])
                print(str_content)
                output(count,i,size_a,size_b,size_delta)
                old_folder_path=folder_path_b #remove b
                if not move_folder(old_folder_path, new_folder_path):
                    print(move_folder(old_folder_path, new_folder_path1))
            else:
                str_content = str(mark[1])
                print(str_content)
                output(count,i,size_a,size_b,size_delta)
        else:

            str_content = str(mark[1])
            print(str_content)
            output(count,i,size_a,size_b,size_delta)
            # old_folder_path=folder_path_a #remove a
            # move_folder(old_folder_path, new_folder_path)
            # print(i,format_bytes(size_a),"?",format_bytes(size_b))
            # #double check 
    # print("level1 check", ""," is done")


def level2_process_folder(folder_name,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count):
    
    root_choose1=root_mydrive+distination_path
    root_choose1=os.path.join(root_choose1, folder_name)
    print("orginal_choose:", root_choose1)

    root_to_compare1= root_migration+comparesource_path
    root_to_compare1=os.path.join(root_to_compare1, folder_name)
    print("root_to_compare:", root_to_compare1)

    for i in same_list_creation(root_choose1,root_to_compare1):
        root_choose2=os.path.join(root_choose1, i)
        root_to_compare2=os.path.join(root_to_compare1, i)
        level1_folder_to_Process(root_choose2,root_to_compare2,root_to_remove,root_to_remove1,count)

    print("Folder level2 check", folder_name," is done")


def level3_process_folder(folder_name,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count):
    root_choose1=root_mydrive+distination_path
    root_choose1+=folder_name
    
    distination_path+=folder_name
    print("orginal_choose:", root_choose1)

    root_to_compare1= root_migration+comparesource_path
    root_to_compare1+=folder_name
    comparesource_path+=folder_name
    print("root_to_compare:", root_to_compare1)

    for i in same_list_creation(root_choose1,root_to_compare1):
        level2_process_folder(i,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count)

    print("Folder level3 check", folder_name," is done")


def output(count,i,size_a,size_b,size_delta):
    print(count[0],":", "",format_bytes(size_a),"<>",format_bytes(size_b),'size delta=',format_bytes(size_delta), size_delta)


def folder_contents_compare(folder_name,root_mydrive,root_migration):
    root_choose1=root_mydrive+"Video\\Torrent_F\\"
    root_choose1+=folder_name
    print("orginal_choose:", root_choose1)

    root_to_compare1= root_migration+"Torrent_F\\"
    root_to_compare1+=folder_name
    print("root_to_compare:", root_to_compare1)


#  main开始



# folder_to_Process=['无码','FC2']
# for folder_name in folder_to_Process:
#     count=[0]
#     root_choose1=root_mydrive+"Video\\Torrent_F\\"
#     root_choose1+=folder_name

#     root_to_compare1= root_migration+"Torrent_F\\"
#     root_to_compare1+=folder_name
#     level1_folder_to_Process(root_choose1,root_to_compare1,root_to_remove,root_to_remove1,count)


distination_path="West\\"
comparesource_path="To Process\\West\\"
folder_to_Process=['~神秘代碼C']
for i in folder_to_Process:
    count=[0]
    level2_process_folder(i,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count)


folder_to_Process=['Runed']
for folder_name in folder_to_Process:
    count=[0]
    root_choose1=root_mydrive+"West\\"
    root_choose1+=folder_name

    root_to_compare1= root_migration+"To Process\\West\\"
    root_to_compare1+=folder_name
    level1_folder_to_Process(root_choose1,root_to_compare1,root_to_remove,root_to_remove1,count)




# folder_to_Process=['2000-2019里番']
# for folder_name in folder_to_Process:
#     count=[0]
#     root_choose1=root_mydrive+""
#     root_choose1+=folder_name

#     root_to_compare1= root_migration+""
#     root_to_compare1+=folder_name
#     level2_folder_to_Process(root_choose1,root_to_compare1,root_to_remove,root_to_remove1,count)


# distination_path=""
# comparesource_path=""
# folder_to_Process=['Movie','TV']
# for i in folder_to_Process:
#     count=[0]
#     level2_process_folder(i,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count)



# distination_path=""
# comparesource_path=""
# folder_to_Process=['Movie','TV']
# for i in folder_to_Process:
#     count=[0]
#     level3_process_folder(i,distination_path, comparesource_path,root_mydrive,root_migration,root_to_remove,root_to_remove1,count)