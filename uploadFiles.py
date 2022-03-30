import sys
import os
import shutil
sys.path.append('C:/Users/Niraj/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages')
import dropbox

class TransferData:
        def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, files_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for roots, dirs, files in os.walk(files_from):
            f = open(file_from,'rb')
            # file name and path from the given path 
        #relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
        

def main():
    access_token ='sl.BEyDdpAlyHkn3j1_chfa3YGufpP-hbQw1WLIhl113R7s6k2ZYK01MpQ78AKIuyFcqPti68FFWsYs8XZ-2XO3sBOcQmwOo_pB8E8BqWgjojk4SIY-OQzBnbHTmeNahyaXud9PEnEAe2bQ'
    transferData = TransferData(access_token)
    file_from = input("Enter the file to be uploaded from :- ")
    file_to = input("Enter the full path to upload to dropbox:- ")
    transferData.upload_file(file_from,file_to)

main()



    
