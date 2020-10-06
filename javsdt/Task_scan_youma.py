from functions_scan import scan_path
from functions_preparation import choose_directory

#Just pure scan the file 
#output will be a list csv file


# 用户输入“回车”就继续选择文件夹整理
input_start_key = ''
while input_start_key == '':
    # 用户选择需要整理的文件夹
    print('请选择要整理的文件夹：', end='')
    root_choose = choose_directory()
    print(root_choose)
    csv_name="testexport"
    scan_path(root_choose,csv_name)

    
    input_start_key = input('回车继续选择文件-夹整理：')
    