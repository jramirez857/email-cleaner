import os.path as p
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Sets the scope and application name for the project. This is required
# for the flow to create the necessary credentials.
SCOPES = ['https://mail.google.com/']
APPLICATION_NAME = 'Gmail API Python'

class GmailAuth:
    """
    The GmailAuth class is used to authenticate with the Gmail API.
    """
    def __init__(self):
        self.credentials = self.get_credentials()
        self.service = self.get_service()
    
    def get_credentials(self):
        """
        Checks if the token.json file exists and uses it if it does.
        If it doesnt, it checks for the credentials.json file, runs through the flow and
        saves the credentials for the next run.
        """
        creds = None
        if p.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        return creds

    def get_service(self):
        """
        Returns the service object for the email API.
        """
        return build('gmail', 'v1', credentials=self.credentials)

if __name__ == '__main__':
    auth = GmailAuth()