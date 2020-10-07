## Create a new Document in Google Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def scan(drive):
      # Auto-iterate through all files in the root folder.
      file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
      for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))


def copy(folder,title,fileID):
      drive.auth.service.files().copy(fileId=fileID,
                           body={"parents": [{"kind": "drive#fileLink",
                                 "id": folder}], 'title': title}).execute()

folder = "1GMP8XuhnwNwk78zLnVu45vI7hKG8b7OX"
title = "testfile" #files real name
fileID = "1wvMQctR5F_pHGYVilwffpxPwOoCrBBCR"

scan(drive)
