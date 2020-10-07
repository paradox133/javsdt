# To compare size of folders and remove the smaller video ACROSS DIFFERENT GOOGLE DRIVE for Suren and Youma
#Fully Auto
import os, re, sys
from os.path import exists
from re import findall
from re import search
from configparser import RawConfigParser
from shutil import copyfile
from traceback import format_exc
from tkinter import filedialog, Tk

from functions_scan import get_size, format_bytes, list_creation, move_folder,same_list_creation

sep = os.sep
sys.stdout = open('log/CompareList.txt', 'w')


def process_folder(folder_name):
    
    root_choose1="G:\My Drive\Video\Torrent_F\\"
    root_choose1+=folder_name
    print("orginal_choose:", root_choose1)

    root_to_compare1= "G:\Shared drives\Migration\Torrent_F\\"
    root_to_compare1+=folder_name
    print("root_to_compare:", root_to_compare1)

    root_to_remove="G:\Shared drives\Migration\To remove"
    print("root_to_remove:", root_to_remove)
    root_to_remove1="G:\Shared drives\Migration\To remove1"
    print("root_to_remove1:", root_to_remove1)

    count=0
    for i in same_list_creation(root_choose1,root_to_compare1):
        root_choose2=os.path.join(root_choose1, i)
        root_to_compare2=os.path.join(root_to_compare1, i)
        for i in same_list_creation(root_choose2,root_to_compare2):
            folder_path_a=os.path.join(root_choose2, i)
            folder_path_b=os.path.join(root_to_compare2, i)
            size_a=get_size(folder_path_a) 
            size_b=get_size(folder_path_b) 
            new_folder_path=os.path.join(root_to_remove,i) 
            new_folder_path1=os.path.join(root_to_remove1,i) 
            count=count+1
            if count<20000:
                if 1.01*size_a>size_b:
                    print(count,":", i,format_bytes(size_a),">",format_bytes(size_b))
                    old_folder_path=folder_path_b #remove b
                    if not move_folder(old_folder_path, new_folder_path):
                        print(move_folder(old_folder_path, new_folder_path1))
                    
                else:
                    print(count,":", i,format_bytes(size_a),"<",format_bytes(size_b))
                    # old_folder_path=folder_path_a #remove a
                    # move_folder(old_folder_path, new_folder_path)

                    # print(i,format_bytes(size_a),"?",format_bytes(size_b))
                    # #double check 
            else:
                break
    print("Folder", folder_name," is done")


#  main开始
print('start')
folder_to_Process=['有码','素人']
for i in folder_to_Process:
    process_folder(i)
print("End")