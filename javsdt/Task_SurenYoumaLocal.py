#no DB Check for all new downloaded files
#do local clean for under 200MB Folders after processing

from jav321_suren import process_suren
from javbus_youma import process_youma
from functions_clean import cleanfolder


root_choose = "V:\Torrent\Auto"
foldersize=209715200 #(200MB=1024^2*200)

print(root_choose)
process_suren(root_choose)
process_youma(root_choose)

print(cleanfolder(root_choose,foldersize)) #clean  folder size less than 200MB
    
