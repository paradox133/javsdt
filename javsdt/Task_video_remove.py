# To compare size of folders and remove the smaller video ACROSS DIFFERENT GOOGLE DRIVE 
#Fully Auto
import os, re,sys
import shutil
from os.path import exists


sep = os.sep
sys.stdout = open('log/VideoToRemove.txt', 'w')

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
    scope= next(os.walk(path))[1]
    return scope

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