from gmail_auth import GmailAuth
from progressbar import ProgressBar
import logging

logging.basicConfig(level=logging.INFO)

gmail_client = GmailAuth()

def get_batch_messages():
    """
    Gets a batch of messages from the Gmail API for the logged in user.
    """
    response = gmail_client.service.users().messages().list(userId='me').execute()
    messages = []
    while 'nextPageToken' in response:
        messages.extend(response['messages'])
        response = gmail_client.service.users().messages().list(userId='me', pageToken=response['nextPageToken']).execute()
    
    return messages


if __name__ == '__main__':
    messages = get_batch_messages()
    for message in messages:
        print(type(message), message)
    logging.info('Found %d messages', len(messages))