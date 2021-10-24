from collections import defaultdict, OrderedDict
from gmail_auth import GmailAuth
from progressbar import ProgressBar
import pprint
import logging

logging.basicConfig(level=logging.INFO)

gmail_client = GmailAuth()
pp = pprint.PrettyPrinter(indent=4)
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

def get_senders():
    """
    Gets a list of senders from the Gmail API for the logged in user.
    """
    senders = defaultdict(int)
    messages = get_batch_messages()
    for message in messages:
        email = gmail_client.service.users().messages().get(userId='me', id=message['id']).execute()
        for key, value in email.items():
            if key == 'payload':
                for key2, value2 in value.items():
                    if key2 == 'headers':
                        for header in value2:
                            if header['name'] == 'From':
                                senders[header['value']] += 1
    return senders

def get_top_senders(senders, top_n):
    """
    Gets the top senders from the Gmail API for the logged in user.
    """
    return OrderedDict(
        sorted(senders.items(), key=lambda x: x[1], reverse=True), top_n
    )


if __name__ == '__main__':
    senders = get_senders()
    top_senders = get_top_senders(senders, 10)
    pp.pprint(top_senders)
    logging.info('Found %d senders', len(senders))