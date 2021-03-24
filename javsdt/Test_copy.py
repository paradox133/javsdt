

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def get_drive_handle():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def copy_file(service, source_id, dest_title):
    copied_file = {'title': dest_title}
    f = service.files().copy(fileId=source_id, body=copied_file).execute()
    return f['id']
                            
def main(dest_title,fileID,drive):


    source = drive.CreateFile({'id': fileID})
    print(source)

    dest_id = copy_file(drive.auth.service, fileID, dest_title)
    dest = drive.CreateFile({'id': dest_id})
    dest.FetchMetadata('title')
    print(dest)


dest_title = "testfile"
fileID = "1zlB8PzhjHyHM6I-m827ud1YdYE1X-Cj1"
drive = get_drive_handle()

main(dest_title,fileID,drive)