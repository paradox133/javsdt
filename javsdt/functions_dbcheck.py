# -*- coding:utf-8 -*-
import pandas as pd
import sqlite3 
from functions_process import find_num_bus, find_num_suren

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

def retieve_sql_table_key(table_name):
    conn = sqlite3.connect('TestDB.db')  
    df = pd.read_sql_query("select file_id, file_path from " +table_name+";", conn)
    return df.values.tolist()

def retieve_sql_table_column(table_name,key_value):
    conn = sqlite3.connect('TestDB.db')  
    cursor = conn.cursor() 
    cursor.execute("select file_path from " +table_name+" where file_id=''"+key_value+ "'';", conn)
    result=cursor.fetchall()
    return str(result[0])

def process_sql_table_column(table_name):
    custom_file_type = "MP4、MKV、AVI、WMV、ISO、RMVB、FLV、TS、RM"
    custom_surplus_words="XHD1080、MM616、FHD-1080、BIG-2048、big2048、FENGNIAO、nyap2p.com、UUE29、UUF39、UUF87、UUP87、UUW62、UUS75、UUV97、VIP1196、A57X"
    custom_suren_pref="BMH、BNJC、CUTE、DCV、EMOI、EVA、EWDX、EXMU、EZD、FAD、FCTD、GANA、GAREA、GAV、GERBM、GERK、HEN、HMDN、HOI、HSAM、HYPN、IMDK、INST、ION、\
        JAC、JKK、JKZ、JOTK、KAGD、KJN、KNB、KSKO、KURO、LADY、LAFBD、LAS、LUXU、MAAN、MGDN、MISM、MIUM、MMGH、MMH、MNTJ、MTP、MY、NAMA、NNPJ、NTK、NTTR、OBUT、\
        ORE、OREBMS、OREC、OREP、ORERB、ORETD、ORETDP、OREX、OTIM、PAPA、PER、PKJD、REP、SCP、SCUTE、SHOW、SHYN、SIMM、SIRO、SPOR、SPRM、SQB、SRCN、SRHO、SRTD、SSAN、STKO、SUKE、SVMM、SWEET、SYBI、URF、VOV、YKMC"
    tuple_type = tuple(custom_file_type.split('、'))        # 需要扫描的文件的类型
    list_surplus_words = custom_surplus_words.split('、')
    list_suren_num = custom_suren_pref.split('、') 
    df=retieve_sql_table_key(table_name)  
    rowcount=len(df)
    # print(df[0])
    count=0
    for key_value in df:
        i=key_value[1]
        file_temp = i.upper()
        if 'FC2' in file_temp:
            continue    # 【跳出2】
        for word in list_surplus_words:
            file_temp = file_temp.replace(word, '')
        # jav_num 视频中的车牌
        jav_num=""
        jav_num= find_num_suren(file_temp, list_suren_num)
        count+=1
        if not jav_num:
            jav_num = find_num_bus(file_temp, list_suren_num)
        conn = sqlite3.connect('TestDB.db')  
        cursor = conn.cursor() 
        sqlcommand="UPDATE "+ table_name +" SET ID ='"+ str(jav_num) + "' WHERE file_id = '"+ key_value[0]+"'"
        cursor.execute(sqlcommand)
        conn.commit()
        print(count, ":",jav_num)

