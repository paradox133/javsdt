#create folder list to feed emby
import os, re
import sys
from os.path import exists
import re
from shutil import copyfile
import xml.etree.ElementTree as ET
from functions_scan import list_creation



def List_filter(folderlist, patternName):
    if folderlist is None:
        return None
    else:
        newlist=[]
        for i in folderlist:
            if patternName.match(i): 
                newlist.append(i)
                # print(newlist)
        return newlist

# path_generate
def media_path_gen(scope,path):
    str_path=""
    if scope is None:
        return ""
    else:
        for i in scope:
            FolderPrefix=i
            str_path+="    <MediaPathInfo> \n     <Path>"+     path+ i+"</Path>\n    </MediaPathInfo>\n"
        return str_path

# main output function
def output(patternName, fileNameString,root_choose1,root_choose2,path1,path2):

    List1=List_filter(list_creation(root_choose1),patternName)
    List2=List_filter(list_creation(root_choose2),patternName)
    stroutput=media_path_gen(List1,path1)+media_path_gen(List2,path2)
    print(stroutput)
    # print(len(List1)+len(List2))
    return stroutput


#  create folder list for emby lib youma
def EmbyYoumaListCreation():
    root_choose1="G:\My Drive\Video\Torrent_F\有码"
    root_choose2="G:\Shared drives\Migration\Torrent_F\有码"
    path1="/volume1/GDrive1/Video/Torrent_F/有码/"
    path2="/volume1/GDrive2/Torrent_F/有码/"
    List=[]
    patternA = re.compile("^([A-C])")
    patternB = re.compile("^([D-F])")
    patternC = re.compile("^([G-I])")
    patternD = re.compile("^([J-K])")
    patternE = re.compile("^([L-M])")
    patternF = re.compile("^([N-Q])")
    patternG = re.compile("^([R])")
    patternH = re.compile("^([S])")
    patternI = re.compile("^([T])")
    patternJ = re.compile("^([U-Z|0-9])")
    patternList=[patternA,patternB,patternC,patternD,patternE,patternF,patternG,patternH,patternI,patternJ]
    
    fileNameString='list/EmbyYoumaList'
    count=1
    for i in patternList:
        fileName=fileNameString+str(count)+'.txt'
        f=open(fileName, 'w')
        sys.stdout = f
        List.append(output(i,fileName,root_choose1,root_choose2,path1,path2))
        count+=1
        f.close
    return List

#  create folder list for emby lib youma
def EmbySurenListCreation():
    root_choose1="G:\My Drive\Video\Torrent_F\素人"
    root_choose2="G:\Shared drives\Migration\Torrent_F\素人"
    path1="/volume1/GDrive1/Video/Torrent_F/素人/"
    path2="/volume1/GDrive2/Torrent_F/素人/"
    List=[]

    patternA = re.compile("^([A-M])")
    patternB = re.compile("^([N-Z|0-9])")
    patternList=[patternA,patternB]
    
    fileNameString='list/EmbySurenList'
    count=1
    for i in patternList:
        fileName=fileNameString+str(count)+'.txt'
        f=open(fileName, 'w')
        sys.stdout = f
        List.append(output(i,fileName,root_choose1,root_choose2,path1,path2))
        count+=1
        f.close
    return List

#xml process
def copymodelxml(modelpath,libname,destinationpath):
    destinationfolder=destinationpath+'\\'+ libname
    if not exists(destinationfolder):
        os.makedirs(destinationfolder)
    destinationfilepath=destinationfolder+'\\options.xml'
    # if exists(destinationfilepath):
    #     os.remove(destinationfilepath)
    copyfile(modelpath, destinationfilepath)
    return destinationfilepath

def revisexml(xml_filepath,libname):
    # libnamereplacestring='<Name>'+libname+'</Name>'
    # with open(xml_filepath, encoding='utf-8') as f:


    # register_all_namespaces(xml_filepath)
    tree = ET.parse(xml_filepath)
    root = tree.getroot()
    #     root = tree.getroot()
    for name in root.findall('Name'):
        try:
            name.text = libname
            # print(name)
            # print(name.text)
        except AttributeError:
            pass
    
    tree.write(xml_filepath, encoding='utf-8')
    # f=open(xml_filepath, 'w')
    # sys.stdout = f    
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    # f.close()
    # f=open(xml_filepath, "r+")
    # for line in f.readlines():
    #     line=line.replace('<Name>Libname</Name>',libnamereplacestring,1)
 
# def register_all_namespaces(filename):
#     my_namespaces = dict([node for _, node in ET.iterparse(filename,
#                                                         events=['start-ns'])])
    return xml_filepath

# def replacetext(filepath,targetsstring, replacestring):
#     f=open(filepath, 'r+')
#     for line in f:
#         if targetsstring in line:
#             line=line.replace(targetsstring,replacestring)
#         f.write(line)
#     f.close

def replacetext(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r', encoding="utf-8")
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w', encoding="utf-8")
    file_handle.write(file_string)
    file_handle.close()
    

#  main开始
modelpath='C:\\Users\\Richard\\Desktop\\emby\\default\\model\\options.xml'
liblist=['YouAC','YouDF','YouGI','YouJK','YouLM','YouNQ','YouR','YouS','YouT','YouUZ']
destinationpath='E:\VS Projects\Vscode\javsdt\list'
# orig_stdout = sys.stdout
# sys.stdout=orig_stdout

# libname='YouAC'
index=0
for libname in liblist: 
    filepath=revisexml(copymodelxml(modelpath,libname,destinationpath),libname)

    targetsstring="<LibraryOptions>"
    replacestring="<?xml version=\"1.0\"?> \n<LibraryOptions xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">"
    replacetext(filepath,targetsstring, replacestring)

    targetsstring="    <MediaPathInfo>x</MediaPathInfo>\n"
    replacestring=EmbyYoumaListCreation()[index]
    replacetext(filepath,targetsstring, replacestring)
    index+=1

index=0
surenliblist=['SurenAM','SurenNZ']
for libname in surenliblist: 
    filepath=revisexml(copymodelxml(modelpath,libname,destinationpath),libname)

    targetsstring="<LibraryOptions>"
    replacestring="<?xml version=\"1.0\"?> \n<LibraryOptions xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">"
    replacetext(filepath,targetsstring, replacestring)

    targetsstring="    <MediaPathInfo>x</MediaPathInfo>\n"
    replacestring=EmbySurenListCreation()[index]
    replacetext(filepath,targetsstring, replacestring) 
    index+=1

#Fix
#need to make sure the xml is decoded by utf-8 #checked