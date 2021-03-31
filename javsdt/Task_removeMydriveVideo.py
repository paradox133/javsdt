# To compare size of folders and remove the smaller video ACROSS DIFFERENT GOOGLE DRIVE 
#Fully Auto
import os
import shutil
from functions_scan import get_size, format_bytes, list_creation, move_folder,same_list_creation
from Task_SurenYoumaLocal import task_surenYoumaLocalMain

sep = os.sep
# sys.stdout = open('log/VideoToRemove.txt', 'w')

# check the multiple cd folder and move it to Auto first
def process_multiple_cd_folders(root):
    target_path=root+"AriaData\Complete"
    dest_path=root+"Auto"
    count=1
    for i in list_creation(target_path):
        i_str=str(i).upper()
        if not "VR" in i_str: # VR can be skipped
            if not (i_str.endswith('-C')or i_str.endswith('UNCENSORED')): # CHINESE AND UNCENSORED ONE SKIPPED IN THIS LOGIC
                if i_str.endswith('A')or i_str.endswith('B')or i_str.endswith('C')or i_str.endswith('D')or i_str.endswith('E'):
                    old_folder_path=os.path.join(target_path, i)  
                    new_folder_path=os.path.join(dest_path, i)  
                    try:
                        if not move_folder(old_folder_path, new_folder_path):
                            print("please check folder",i)
                        print(count,": folder ", i," is potential multiple cd folder and it has been moved")
                    except OSError as e:
                        print("Error: %s : %s" % (new_folder_path, e.strerror))
                    count=count+1

    print("potential multiple cd folder has been moved")
    
#  main
# compare the local with my google drive
# if file exist and size is the same, then delete the local version. 
def process_folder(folder_name):
    root="V:\Torrent\\"
    root_google="G:\My Drive\\"

    print(folder_name,'multipe cd folder check is started')
    process_multiple_cd_folders(root)
    print(folder_name,'multipe cd folder check is ended')
    print(folder_name,'Temporary move is started')
    root_choose1=root_google+"Video\Torrent_F\\"
    root_choose1+=folder_name
    print("orginal_choose:", root_choose1)
    root_to_compare1= root+"Format\\"
    root_to_compare1+=folder_name
    print("root_to_compare:", root_to_compare1)
    root_to_remove=root+"ToRemove"
    print("root_to_remove:", root_to_remove)
    root_to_remove1=root+"ToRemove1"
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

def task_organize_videos():
    folder_to_Process=['有码','素人']
    for i in folder_to_Process:
        process_folder(i)
    #start to organize the videos
    task_surenYoumaLocalMain()

task_organize_videos()