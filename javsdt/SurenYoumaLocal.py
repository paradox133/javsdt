#no DB Check for all new downloaded files
#do local clean for under 200MB Folders after processing

from jav321_suren import process_suren
from javbus_youma import process_youma
from functions_preparation import choose_directory
from functions_clean import clean



# 用户输入“回车”就继续选择文件夹整理
# input_start_key = ''
# while input_start_key == '':
#     # 用户选择需要整理的文件夹
#     print('请选择要整理的文件夹：', end='')
root_choose = "V:\Torrent\Auto"
print(root_choose)
process_suren(root_choose)
process_youma(root_choose)
print(clean(root_choose)) #clean  folder size less than 200MB
    
    # input_start_key = input('回车继续选择文件-夹整理：')