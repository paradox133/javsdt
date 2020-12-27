#no DB Check for all new downloaded files
#do local clean for under 200MB Folders after processing

from jav321_suren import process_suren
from javbus_youma import process_youma
from functions_clean import cleanfolder


# root_choose = "V:\Torrent\Auto"
root_choose = "V:\Torrent\AriaData\Complete"
foldersize=270532608 #(258MB=1024^2*258)

print(root_choose)
process_suren(root_choose)
process_youma(root_choose)

print(cleanfolder(root_choose,foldersize)) #clean  folder size less than 200MB
    
