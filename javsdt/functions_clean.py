# -*- coding:utf-8 -*-
import os, re, sys
import shutil  
from os.path import exists
from re import findall



def clean(root_choose):

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
        folder_list=[]
        scope= next(os.walk(path))[1]
        return scope

    # move_folder
    def move_folder(old_folder_path, new_folder_path):
        if(old_folder_path!=new_folder_path) and (not exists(new_folder_path)):
            os.rename(old_folder_path, new_folder_path)
            print(old_folder_path +" is removed to "+ new_folder_path)
            return True
        else:
            print("Error:"+ old_folder_path +" is removed to "+ new_folder_path)
            return False
            
    #  main开始

    print('clean start')
    print("orginal_choose:", root_choose)
    sep = os.sep
    #sys.stdout = open('VideFodlerSizeList.txt', 'w')
    count=0
    for i in list_creation(root_choose):
        root_choose2=os.path.join(root_choose, i)
        size=get_size(root_choose2) 
        count=count+1
        if size <=209715200: #(200MB=1024^2*200)
            print(count,":", i, "size:",format_bytes(size))
            try:
                shutil.rmtree(root_choose2)
                print(count,":", i,"has been removed from", root_choose2)
            except OSError as e:
                print("Error: %s : %s" % (root_choose2, e.strerror))
    print("done")
    #sys.stdout.close() 
    return True


