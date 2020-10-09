from jav321_suren_google import process_suren
from javbus_youma_google import process_youma
from functions_preparation import choose_directory


# need to fix the cd1 cd2 order bug

config_path='E:\VS Projects\Vscode\javsdt\javsdt\【点我设置整理规则】 google.ini' #my drive
#config_path='E:\VS Projects\Vscode\javsdt\javsdt\【点我设置整理规则】 migration.ini' #my migration
#config_path='E:\VS Projects\Vscode\javsdt\javsdt\【点我设置整理规则】 local.ini' #my drive


# 用户输入“回车”就继续选择文件夹整理
input_start_key = ''
while input_start_key == '':
    # 用户选择需要整理的文件夹
    print('请选择要整理的文件夹：', end='')
    root_choose = choose_directory()
    print(root_choose)
    process_suren(root_choose,config_path)
    process_youma(root_choose,config_path)
    
    input_start_key = input('回车继续选择文件-夹整理：')