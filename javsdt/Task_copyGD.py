## Create a new Document in Google Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
folder = "1GMP8XuhnwNwk78zLnVu45vI7hKG8b7OX"
title = "SHKD-570" #files real name
file = "1YHBYr16eOxlq5ZftLgC5DO7Na60UynSt"
drive.auth.service.files().copy(fileId=file,
                           body={"parents": [{"kind": "drive#fileLink",
                                 "id": folder}], 'title': title}).execute()