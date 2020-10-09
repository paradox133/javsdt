from functions_preparation import choose_directory
from functions_clean import cleanfolder



# 用户输入“回车”就继续选择文件夹整理
# input_start_key = ''
# while input_start_key == '':
#     # 用户选择需要整理的文件夹
#     print('请选择要整理的文件夹：', end='')
root_choose = "G:\My Drive\SHARE COPY"
foldersize=247 #(247B)


print(cleanfolder(root_choose,foldersize)) #clean  folder size less than 200MB