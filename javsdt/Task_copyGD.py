## Create a new Document in Google Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from functions_process import find_num_bus
from functions_dbcheck import pure_check_if_ID_exist
from apiclient import errors
import os
import httplib2
from oauth2client import file,client, tools
from googleapiclient  import discovery




def get_drive_handle():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive


def checkifvideo(fileNameWithExtension):
      custom_file_type = "MP4、MKV、AVI、WMV、ISO、RMVB、FLV、TS、RM"
      tuple_type = tuple(custom_file_type.split('、'))
      file_temp = fileNameWithExtension.upper()
      if file_temp.endswith(tuple_type) and not file_temp.startswith('.'):
            return True
      else:
            return False 

def checkifindb(fileNameWithExtension):
      custom_suren_pref="BMH、BNJC、CUTE、DCV、EMOI、ENDX、EVA、EWDX、EXMU、EZD、FAD、FCTD、GANA、GAREA、GAV、GERBM、GERK、HEN、HMDN、HOI、HSAM、HYPN、IMDK、INST、ION、\
        JAC、JKK、JKZ、JOTK、KAGD、KJN、KNB、KSKO、KURO、LADY、LAFBD、LAS、LUXU、MAAN、MGDN、MISM、MIUM、MMGH、MMH、MNTJ、MTP、MY、NAMA、NNPJ、NTK、NTTR、OBUT、\
        ORE、OREBMS、OREC、OREP、ORERB、ORETD、ORETDP、OREX、OTIM、PAPA、PER、PKJD、REP、SCP、SCUTE、SHOW、SHYN、SIMM、SIRO、SPOR、SPRM、SQB、SRCN、SRHO、SRTD、SSAN、STKO、SUKE、SVMM、SWEET、SYBI、URF、VOV、YKMC"
      table_name="DISTINCTID"
      list_suren_num = custom_suren_pref.split('、') 
      file_temp = fileNameWithExtension.upper()
      jav_num = find_num_bus(file_temp, list_suren_num)
      jav_raw_num = jav_num  # 车牌  abc-123
      return [pure_check_if_ID_exist(jav_raw_num,table_name),jav_raw_num ]


def scan(drive,shareddriveID):
      # Auto-iterate through all files in the root folder.
      file_list = drive.ListFile({
            'q': "trashed=false",
            'corpora': 'teamDrive', 
            'teamDriveId':shareddriveID, 
            'includeTeamDriveItems': True, 
            'supportsTeamDrives': True,
            'maxResults': 1000}).GetList()
            # }).GetList()
      print("number:",len(file_list))
      for file1 in file_list:
            if checkifvideo(file1['title']):
                  if checkifindb(file1['title'])[0]:
                        print('ID: %s, title: %s, id: %s' % (checkifindb(file1['title'])[1],file1['title'], file1['id']))

# Only works for internal mydrive
def copy(drive,folder,title,fileID):
      drive.auth.service.files().copy(fileId=fileID,
                           body={"parents": [{"kind": "drive#fileLink",
                                 "id": folder}], 'title': title}).execute()

def copy_file(service, origin_file_id, copy_title):
  copied_file = {'title': copy_title}
  try:
    return service.files().copy(
        fileId=origin_file_id, body=copied_file).execute()
  except errors.HttpError as error:
    print ('An error occurred: %s' % error)
  return None

def initiate():
      SCOPES = 'https://www.googleapis.com/auth/drive'
      CLIENT_SECRET_FILE = 'client_secret.json'
      APPLICATION_NAME = 'Drive API Python Quickstart'
      # CLIENT_SECRET='client_secret.json'
      store=file.Storage('storage.json')
      creds=store.get()
      if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            creds = tools.run_flow(flow, store)
      # credentials = get_credentials()
      http = creds.authorize(httplib2.Http())
      service = discovery.build('drive', 'v3', http=http)
      return service





shareddriveID='0ABuBYv9uqJ2qUk9PVA'
folder = "1GMP8XuhnwNwk78zLnVu45vI7hKG8b7OX"
title = "testfile" #files real name
# fileID = "1h4sRCM_YvAGXQ6eTnJPZgqg9OzBh4xYX" #mydrive
fileID='15_eMeAwzMTAhk6rJdvRKPsvSh9yFNgeN' #drxterdrive


drive = get_drive_handle()
# copy_file(initiate(), fileID, title)
copy(drive,folder,title,fileID)
# scan(drive,shareddriveID) #working
