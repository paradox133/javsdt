# -*- coding:utf-8 -*-
import os
import shutil  
from functions_scan import get_size, format_bytes, list_creation, move_folder,same_list_creation

#cleanPathOneLevelDown
def cleanfolder(root_choose,foldersizelimit):
          
    #  main开始

    print('clean start')
    print("orginal_choose:", root_choose)
    sep = os.sep
    #sys.stdout = open('VideFodlerSizeList.txt', 'w')
    count=0
    for i in list_creation(root_choose):  #root_choose=V:\Torrent\Auto i=ABP001
        root_choose2=os.path.join(root_choose, i)
        size=get_size(root_choose2) 
        count=count+1
        if size <=foldersizelimit:
            print(count,":", i, "size:",format_bytes(size))
            try:
                shutil.rmtree(root_choose2)
                print(count,":", i,"has been removed from", root_choose2)
            except OSError as e:
                print("Error: %s : %s" % (root_choose2, e.strerror))
    print("done")
    #sys.stdout.close() 
    return True




