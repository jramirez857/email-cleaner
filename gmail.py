"""
This module contains the GmailAuth class. It is used to authenticate with
Gmail.
"""
import argparse
import os.path as p
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Sets the scope and application name for the project. This is required
# for the flow to create the necessary credentials.
SCOPES = ["https://mail.google.com/"]
APPLICATION_NAME = "Gmail API Python"


class Gmail:
    """
    The GmailAuth class is used to authenticate with the Gmail API.
    """

    def __init__(self, **kwargs):
        self.credentials_path = kwargs.get("credentials", "credentials.json")
        self.service = self.get_service()

    def get_credentials(self, token_file="token.json"):
        """
        Checks if the token.json file exists and uses it if it does.
        If it doesnt, it checks for the credentials.json file, runs through the flow and
        saves the credentials for the next run.
        """
        user_credentials = None
        if p.exists(token_file):
            user_credentials = Credentials.from_authorized_user_file(token_file, SCOPES)
            if user_credentials.expired and user_credentials.refresh_token:
                user_credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credentials_path, SCOPES
            )
            user_credentials = flow.run_local_server(port=0)
        with open(token_file, "w") as token:
            token.write(user_credentials.to_json())
        return user_credentials

    def get_service(self):
        """
        Returns the service object for the email API.
        """
        return build("gmail", "v1", credentials=self.get_credentials())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authenticates with the Gmail API.")
    parser.add_argument(
        "-c",
        "--credentials",
        type=int,
        default=100,
        help="The filename or path to the credentials.",
    )
    args = parser.parse_args()
    gmail = Gmail(credentials=args.credentials)
