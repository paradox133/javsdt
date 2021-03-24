from apiclient import errors
import os
import httplib2
from oauth2client import file,client, tools
from googleapiclient  import discovery
from function_database import pd_to_db


def trash_file(service, file_id):
#   """Move a file to the trash.
#   Args:
#     service: Drive API service instance.
#     file_id: ID of the file to trash.

#   Returns:
#     The updated file if successful, None otherwise.
#   """
    try:
      return service.files().trash(fileId=file_id).execute()
    except errors.HttpError as error:
      print ('An error occurred: {error}') 
      return None

def initiate():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Drive API Python Quickstart'
    # CLIENT_SECRET='client_secret.json'
    store=file.Storage('storage.json')
    creds=store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    # credentials = get_credentials()
    http = creds.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    file_id=''
    trash_file(service,file_id)
    print('done')

#main
print("start")
database_name='TestDB.db'
table_name='mydrive_trashed'
text_file="D:\googledownload\rclone-v1.53.1-windows-amd64\rclone-v1.53.1-windows-amd64\mydrive_output.txt"
# pd_to_db(database_name,table_name,text_file)
print("end")