
from Richarddb import pd_to_db

#main import and reformat the txt(from rclone) to db 

print("start")
database_name='TestDB.db'
# table_name='mydrive_trashed'
# text_file="D:\\googledownload\\rclone-v1.53.1-windows-amd64\\rclone-v1.53.1-windows-amd64\\mydrive_output.txt"
table_name='migration_trashed'
text_file="D:\\googledownload\\rclone-v1.53.1-windows-amd64\\rclone-v1.53.1-windows-amd64\\migration_output.txt"


pd_to_db(database_name,table_name,text_file)
print("end")