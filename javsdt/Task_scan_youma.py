from functions_scan import scan_path
from functions_preparation import choose_directory

#Just pure scan the file 
#output will be a list csv file

#############################Task###############################################
# Need to improve the efficiency by Pre-check the ID to see if ABC is alrady there

# New feature only check the ID that we have collected. #checked





#Temp list want to skip
skipList=["MD","X","S","D","DAY","HD"]

# 用户输入“回车”就继续选择文件夹整理
input_start_key = ''
while input_start_key == '':
    # 用户选择需要整理的文件夹
    print('请选择要整理的文件夹：', end='')
    root_choose = choose_directory()
    print(root_choose)
    csv_name="testexport_derek"
    scan_path(root_choose,csv_name,skipList)

    
    input_start_key = input('回车继续选择文件-夹整理：')
    