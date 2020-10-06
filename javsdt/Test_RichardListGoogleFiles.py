# from __future__ import print_function
# from googleapiclient import discovery
# from httplib2 import Http
# from oauth2client import file,client, tools

#====================================================
from enum import Enum
import argparse
import time
import logging
import os
import httplib2
from oauth2client import file,client, tools
from googleapiclient  import discovery
from oauth2client.file import Storage


# SCOPES= "https://www.googleapis.com/auth/drive.readonly.metadata"
# CLIENT_SECRET='client_secret.json'
# store=file.Storage('storage.json')
# credz=store.get()

# if not credz or credz.invalid:
#     flow=client.flow_from_clientsecrets(CLIENT_SECRET,SCOPES)
#     credz=tools.run_flow(flow,store)

# SERVICES=discovery.build('drive','v3',http=credz.authorize(Http()))
# files=SERVICES.files().list().execute().get('files', [])
# count=0
# for f in files:
#     count+=1
#     print (count, ":", f['name'],f['mimeType'])


#logging settings
logger = logging.getLogger(__name__); logger.setLevel(logging.DEBUG)    #output DEBUG or higher level messages
fmt = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s - %(levelname)s: %(message)s')
log_sh = logging.StreamHandler();\
    log_sh.setLevel(logging.DEBUG);\
    log_sh.setFormatter(fmt)
log_fh = logging.FileHandler('log\Scandebug.log');\
    log_fh.setLevel(logging.DEBUG);\
    log_fh.setFormatter(fmt)
log_efh = logging.FileHandler('log\Scanerror.log');\
    log_efh.setLevel(logging.ERROR);\
    log_efh.setFormatter(fmt)
logger.addHandler(log_sh); logger.addHandler(log_fh); logger.addHandler(log_efh)


def get_credentials():
    home_FOLDER = os.path.expanduser('~')
    credential_folder = os.path.join(home_FOLDER, '.credentials')
    if not os.path.exists(credential_folder):
        os.makeFOLDERs(credential_folder)
    credential_path = os.path.join(credential_folder, 'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


class FileType(Enum):
    # """
    # file type
    # """
    FILE = 0
    FOLDER = 1


class Node():
    # """
    # class for Google Drive item
    # """
    def __init__(self, path, basename, depth, file_type, file_id):
        self.path = path
        self.basename = basename
        self.depth = depth
        self.file_type = file_type
        self.file_id = file_id
        self.children = []
    
    def print_children(self):
        # """
        # print all children
        # """
        print('{0}{1}    (ID: {2}    file_type: {3})'.format('  '*self.depth, os.path.basename(self.path), self.file_id, self.file_type))
        for child in self.children:
            child.print_children()
    
    def count_children(self):
        # """
        # count all children
        # """
        num_files = 0; num_folders = 0
        for child in self.children:
            if child.file_type == FileType.FILE:
                num_files += 1
            if child.file_type == FileType.FOLDER:
                num_folders += 1
            a,b = child.count_children()
            num_files += a; num_folders += b
        return (num_files, num_folders)

    def complement_children_path_depth(self):
        # """
        # generate children's path and depth information from basename
        # """
        for child in self.children:
            child.path = '{0}/{1}'.format(self.path, child.basename)
            child.depth = self.depth+1
            child.complement_children_path_depth()


def get_whole_tree(drive_service):
    # """
    # get whole Google Drive item tree
    # """
    MAX_PAGE_SIZE_PER_REQUEST = 100
    count=0
    email_address = drive_service.about().get(fields='user(emailAddress)').execute().get('user')['emailAddress']
    root_id = drive_service.files().get(fileId='root', supportsTeamDrives=False, fields='id', ).execute().get('id')
    root = Node(path='root', basename='root', depth=0, file_type=FileType.FOLDER, file_id=root_id)
    #get all items
    nodes = {root_id: (root, None)}
    page_token = None
    while True:
        response = drive_service.files().list(corpus='user', includeTeamDriveItems=False, orderBy='name', pageSize=MAX_PAGE_SIZE_PER_REQUEST, pageToken=page_token, q="trashed=false and '{0}' in owners".format(email_address), spaces='drive', supportsTeamDrives=False, fields="nextPageToken, files(id, name, mimeType, parents)").execute()
        items = response.get('files', [])       
        for item in items:
            count+=1
            file_name = item['name']
            file_id = item['id']
            parent_id = item['parents'][0]
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                file_type = FileType.FOLDER
            else:   
                file_type = FileType.FILE
            node = Node(path=None, basename=file_name, depth=None, file_type=file_type, file_id=file_id)
            nodes[file_id] = (node, parent_id)
            #logger.debug('file_name: {0}, file_id: {1}, parent_id: {2}'.format(file_name, file_id, parent_id))
            print(count,':',file_name,file_type)
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    #connect to parent
    for file_id, (node, parent_id) in nodes.items():
        if parent_id is None:   #root node
            continue
        nodes[parent_id][0].children.append(node)
    root.complement_children_path_depth()
    return root
    
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

start_time = time.time()

root = get_whole_tree(drive_service=service)
root.print_children()
print('\nThere are {0} files and {1} folders.'.format(*root.count_children()))

print('Search took {0} [sec].'.format(time.time()-start_time))