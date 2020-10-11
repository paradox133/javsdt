#create folder list to feed emby
import os, re
import sys
from os.path import exists
import re

#  main开始
print('start')

root_choose1="G:\My Drive\Video\Torrent_F\有码"
root_choose2="G:\Shared drives\Migration\Torrent_F\有码"
path1="/volume1/GDrive1/Video/Torrent_F/有码/"
path2="/volume1/GDrive2/Torrent_F/有码/"


patternA = re.compile("^([A-C])")
patternB = re.compile("^([D-F])")
patternC = re.compile("^([G-I])")
patternD = re.compile("^([J-M])")
patternE = re.compile("^([N-Q])")
patternF = re.compile("^([R-T])")
patternG = re.compile("^([U-Z|0-9])")
patternList=[patternA,patternB,patternC,patternD,patternE,patternF,patternG]
# print("patternA:", patternA)

# create level one folder name list
def list_creation(path):
    scope= next(os.walk(path))[1]
    # print(scope)
    return scope

def List_filter(folderlist, patternName):
    newlist=[]
    for i in folderlist:
        if patternName.match(i): 
            newlist.append(i)
            # print(newlist)
    return newlist

# path_generate
def media_path_gen(scope,path):
    str_path=""
    for i in scope:
        FolderPrefix=i
        str_path+="    <MediaPathInfo> \n     <Path>"+     path+ i+"</Path>\n    </MediaPathInfo>\n"
    return str_path

# main output function
def output(patternName, fileNameString):
    List1=List_filter(list_creation(root_choose1),patternName)
    List2=List_filter(list_creation(root_choose2),patternName)
    sys.stdout = open(fileNameString, 'w')
    # print("List_filter:",List1 , len(List1))
    # print("List_filter:",List2 , len(List2))
    print(media_path_gen(List1,path1))
    print(media_path_gen(List2,path2))
    # print(len(List1)+len(List2))

#main function start
fileNameString='EmbyList'
count=1
for i in patternList:
    filename=fileNameString+str(count)+'.txt'
    output(i,filename)
    count+=1





print("end")