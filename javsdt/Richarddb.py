import sqlite3 
import sys
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('TestDB.db')  
cursor = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - VIDEO FOLDER
cursor.execute('''CREATE TABLE VIDEO_FOLDER
             ([generated_id] INTEGER PRIMARY KEY, [ID] text, [Size] integer)''')
# c.execute('''CREATE TABLE VIDEO_FOLDER
#              ([bus_id] text, [size] integer, [Path] text,[video_count] integer, [modifed_date] date)''')          
                 
conn.commit()

read_clients = pd.read_csv (r'E:\VS Projects\Vscode\javsdt\GlobalScan.csv')
read_clients.to_sql('VIDEO_FOLDER', conn, if_exists='append', index=False) 



print (cursor.execute("select * from VIDEO_FOLDER").rowcount)

