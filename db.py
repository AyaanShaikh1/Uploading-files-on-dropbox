import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        # Initializing Dropbox 
        dbx = dropbox.Dropbox(self.access_token)
        # Statement to open the file and store as 'f' 
        #rb = read binary mode
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A1wbYewWTnAITwkcW_xFO5f9twAovo2uQ_ZefTCtsjk2DLwGMwdjPFrVqpo37TUVb0dUzOvDds057uMNxJt0TR_Hl2b74v9Gp8ODbDz5pBYuO9pnGPj4m3PrFTtnCjvHggyQZBM'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')    # The full path to upload the file to, including the file name        

    # API v2
    transferData.upload_file(file_from, file_to)

main()