import sqlite3 
import sys
import time
import pandas as pd

from functions_scan import read_to_db, db_csv_generation



def db_table_create(database_name,table_name,conn):
    cursor = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    dropcommand='DROP TABLE '+ table_name 
    createcommand='CREATE TABLE '+ table_name +'([file_id] text PRIMARY KEY, [file_path] text, [Size] integer)'
    # cursor.execute(dropcommand) #for the first time has to comment this line of the code
    # Create table - VIDEO FOLDER
    cursor.execute(createcommand)
    conn.commit()

def pd_to_db(database_name,table_name,text_file):
    conn = sqlite3.connect(database_name)  
    db_table_create(database_name,table_name,conn)
    read_clients=read_to_db(text_file)
    read_clients.to_sql(table_name, conn, if_exists='append', index=False) 
    conn.commit()
    print("pd_to_db is done")


def db_process():
    # conn = sqlite3.connect('E:\VS Projects\Vscode\javcrawler\Javbus_crawler\TestDB.db')  
    conn = sqlite3.connect('TestDB.db')  
    cursor = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    cursor.execute('''
                DROP TABLE IF EXISTS "VIDEO_FOLDER"
                ''')
    # Create table - VIDEO FOLDER
    cursor.execute('''
                    CREATE TABLE VIDEO_FOLDER
                ([generated_id] INTEGER PRIMARY KEY, [ID] text, [Size] integer)
                ''')
    # c.execute('''CREATE TABLE VIDEO_FOLDER
    #              ([bus_id] text, [size] integer, [Path] text,[video_count] integer, [modifed_date] date)''')          

    conn.commit()
    db_csv_generation()
    # time.sleep(20)
    read_clients = pd.read_csv (r'E:\VS Projects\Vscode\javsdt\GlobalScan.csv',error_bad_lines=True)
    read_clients.to_sql('VIDEO_FOLDER', conn, if_exists='append', index=False) 


    #remove the duplicates
    cursor.execute('''
                DROP TABLE IF EXISTS "DISTINCTID"
                ''')
    cursor.execute('''
                        CREATE TABLE DISTINCTID AS 
                        SELECT  DISTINCT ID FROM VIDEO_FOLDER
                        ORDER BY ID
                    ''')
    conn.commit()
    # print("db is updated to the latest")



