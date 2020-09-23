# -*- coding:utf-8 -*-
import sqlite3 

def insert_record(ID,table_name,cursor):
    sqlcommand="INSERT INTO "+ table_name +" VALUES ('"+ID+"')"
    cursor.execute(sqlcommand)

def if_ID_exist(ID,table_name):
    conn = sqlite3.connect('TestDB.db')  
    cursor = conn.cursor() 
    sqlcommand="SELECT ID FROM "+ table_name +" WHERE TRIM(ID)="+ "'"+ ID+"'"
    #print("sqlcommand is ", sqlcommand)
    cursor.execute(sqlcommand)
    rows = cursor.fetchall()
    # print("rows is ", rows)
    count = len(rows)
    # print("count is ", count)
    if count>0:
        return True
    else:
        #insert this record to the table 
        insert_record(ID,table_name, cursor)
        conn.commit()
        return False

def pure_check_if_ID_exist(ID,table_name):
    conn = sqlite3.connect('TestDB.db')  
    cursor = conn.cursor() 
    sqlcommand="SELECT ID FROM "+ table_name +" WHERE TRIM(ID)="+ "'"+ ID+"'"
    #print("sqlcommand is ", sqlcommand)
    cursor.execute(sqlcommand)
    rows = cursor.fetchall()
    # print("rows is ", rows)
    count = len(rows)
    # print("count is ", count)
    if count>0:
        return True
    else:
        return False
