
import os, re, sys
import platform

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

    count=0
    # i='ABP'
    for i in list_creation(path):
        # sub_folder_path="G:\My Drive\Video\Torrent_F\有码\ABP"
        sub_folder_path=os.path.join(path, i)
        for j in list_creation(sub_folder_path):
            # sub_folder_path2="G:\My Drive\Video\Torrent_F\有码\ABP\ABP-001"
            sub_folder_path2=os.path.join(sub_folder_path, j)
            size=get_size(sub_folder_path2)
             #cdate=creation_date(sub_folder_path)
            count+=1
            print( j,',', size)



#  main开始
sys.stdout = open('GlobalScan.csv', 'w')
sub_folder_name=['有码','素人']
path=["G:\My Drive\Video\Torrent_F\\","G:\Shared drives\Migration\Torrent_F\\"]
for pathname in path:
    for foldername in sub_folder_name:
        process_folder(pathname,foldername)

