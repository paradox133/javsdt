# To compare size of folders and remove the smaller video ACROSS DIFFERENT GOOGLE DRIVE 
#Fully Auto
import os, re,sys
import shutil
from os.path import exists
from functions_scan import get_size, format_bytes, list_creation, move_folder,same_list_creation
from Task_SurenYoumaLocal import task_surenYoumaLocalMain

sep = os.sep
# sys.stdout = open('log/VideoToRemove.txt', 'w')

    
#  main
# compare the local with my google drive
# if file exist and size is the same, then delete the local version. 
def process_folder(folder_name):
    print(folder_name,'Temporary move is started')

    root_choose1="G:\My Drive\Video\Torrent_F\\"
    root_choose1+=folder_name
    print("orginal_choose:", root_choose1)

    root_to_compare1= "V:\Torrent\Format\\"
    root_to_compare1+=folder_name
    print("root_to_compare:", root_to_compare1)

    root_to_remove="V:\Torrent\ToRemove"
    print("root_to_remove:", root_to_remove)

    root_to_remove1="V:\Torrent\ToRemove1"
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
                if 1.005*size_a>size_b:
                    print(count,":", i,format_bytes(size_a),">",format_bytes(size_b))
                    old_folder_path=folder_path_b #remove b
                    if not move_folder(old_folder_path, new_folder_path):
                        print(move_folder(old_folder_path, new_folder_path1))
                    
                else:
                    print(count,":", i,format_bytes(size_a),"<",format_bytes(size_b))

            else:
                break

    print(folder_name,"Temporary move is done")

    print(folder_name,'Permanent remove is started')

    print("root_to_remove:", root_to_remove)

    count=1
    for i in list_creation(root_to_remove):
        root_to_remove_folder_path=os.path.join(root_to_remove, i)  
        try:
            shutil.rmtree(root_to_remove_folder_path)
            print(count,":", i,"is removed from", root_to_remove)
        except OSError as e:
            print("Error: %s : %s" % (root_to_remove_folder_path, e.strerror))
        count=count+1

    print(folder_name,"Permanent remove is done")

#  main开始
print('start')
folder_to_Process=['有码','素人']
for i in folder_to_Process:
    process_folder(i)
print("End")

#start to organize the videos
task_surenYoumaLocalMain()