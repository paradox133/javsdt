#no DB Check for all new downloaded files
#do local clean for under 200MB Folders after processing

from jav321_suren import process_suren
from javbus_youma import process_youma
from javdb_youma import process_javdb_youma
from functions_clean import cleanfolder

def task_surenYoumaLocalMain():
    # root_choose = "V:Torrent\Auto"
    root_choose = "V:\Torrent\AriaData\Complete"
    foldersize=335000000 #(318MB=1024^2*318)

    print(root_choose)
    process_suren(root_choose)
    process_youma(root_choose)
    process_javdb_youma(root_choose)

    print(cleanfolder(root_choose,foldersize)) #clean  folder size less than 200MB


# task_surenYoumaLocalMain()
    
