from functions_preparation import choose_directory
from functions_clean import cleanfolder



# root_choose = "G:\My Drive\SHARE COPY"
# root_choose = "G:\Shared drives\Migration\Torrent_F\素人"
# root_choose = "G:\Shared drives\Migration\Torrent_F\素人"
# root_choose = "G:\My Drive\Video\FC2 HD Quality #1"
root_choose = "G:\My Drive\Video\FC2 Complete SiteRip November 2018 720p-1080p WEB-DL AAC2 0 H.264 [Censored-Uncensored]-sweety"

foldersize=247 #(247B)

print(cleanfolder(root_choose,foldersize)) #clean  folder size less than 200MB