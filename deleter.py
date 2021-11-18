"""
This module handles the deletion of emails.
"""

import logging
import progressbar
import argparse
from typing import List
from gmail import GmailService

class Deleter:
    """This class handles the deletion of emails. It takes in a list of email senders and deletes it if
    found it within the list of num_emails number of emails.
    """
    def __init__(self, **kwargs) -> None:
        """Initializes the Deleter class.
        Args:
            kwargs (dict): A dictionary of keyword arguments.
                senders (List[str]): A list of email addresses to delete emails from.
                num_emails (int): The number of emails to check through.
                top_n_senders (int): The number of senders to check through default value is 10.
        """
        logging.basicConfig(
            level=kwargs.get("log_level", logging.INFO),
            format="%(funcName)s():%(lineno)i: %(levelname)s: %(message)s",
        )
        self.gmail = kwargs.get("gmail_service", GmailService().get())
        self.top_senders = kwargs.get("top_n_senders", 10)
        logging.info("Getting top %d senders".format(self.top_senders))
        self.senders = kwargs.get("top_n_senders")
        self.emails = self.get_num_emails(kwargs.get('num_emails', 10000))        

    def delete_emails(self, **kwargs) -> None:
        """This method deletes emails from the gmail account.
        It checks through the last self.num_emails number of emails and deletes the emails if they are found in the
        self.senders list.

        Args:
            kwargs (dict): A dictionary of keyword arguments.
                senders (List[str]): A list of email addresses to delete emails from.
                num_emails (int): The number of emails to check through.
                top_n_senders (int): The number of senders to check through.
                progress_bar (bool): Whether or not to display a progress bar.
        """
        logging.info("Deleting the senders from the list in self.senders emails from the gmail account.")
        for i, sender in zip(progressbar.progressbar(self.senders), self.senders):
            logging.info("Deleting emails from sender: {}".format(sender))
            self.delete_emails_from_sender(sender)
    
    def delete_emails_from_sender(self, sender: str) -> None:
        """Deletes emails sent by the passed in sender from the last num_emails list of emails on the 
        gmail account.

        Args:
            sender (str): The email address of the sender to delete emails from.
        """
        logging.info("Deleting emails from sender: {}".format(sender))
        email_ids = self.get_emails_from_sender(sender)

        answer = input("Are you sure you want to delete {} emails from sender: {}? (y/n)".format(len(email_ids), sender))
        if answer == 'y':
            for email_id in email_ids:
                self.delete_email(email_id['id'])
            logging.info("Deleted {} emails from sender: {}".format(len(email_ids), sender))
        else:
            logging.info("Not deleting emails from sender: {}".format(sender))


    def delete_email(self, email_id: str) -> None:
        """Deletes the passed in email from the gmail account.

        Args:
            email_id (str): The id of the email to delete.
        """
        logging.info("Deleting email: {}".format(email_id))
        self.gmail.users().messages().trash(userId='me', id=email_id).execute()

    def get_num_emails(self, num_emails) -> List[str]:
        """Gets the last num_emails from the gmail account.

        Args:
            num_emails (int): The number of emails to get.

        Returns:
            List[str]: A list of emails from the gmail account.
        """
        response = self.gmail.users().messages().list(userId="me").execute()
        logging.info("Getting the last {} emails from the gmail account.".format(num_emails))
        emails = []
        while response.get("nextPageToken", None) and len(emails) < num_emails:
            for message in response["messages"]:
                emails.append(message)
            response = (
                self.gmail.users()
                .messages()
                .list(userId="me", pageToken=response["nextPageToken"])
                .execute()
            )
            logging.debug(
                "Successfully retrieved %d messages", len(response["messages"])
            )

        return emails[-num_emails:]

    def get_email_sender(self, email_id: str) -> str:
        """Gets the email sender of the passed in email id.

        Args:
            email_id (str): The id of the email to get the sender of.

        Returns:
            str: The email address of the sender.
        """
        logging.info("Getting the sender of email: {}".format(email_id))
        email = self.gmail.users().messages().get(userId='me', id=email_id).execute()
        sender = None
        for header in email['payload']['headers']:
            if header['name'] == 'From':
                sender = header['value']
                break
        return sender
    
    def get_emails_from_sender(self, sender: str) -> List[str]:
        """Gets the emails from the last num_emails number of emails sent by the passed in sender.

        Args:
            sender (str): The email address of the sender to get emails from.

        Returns:
            List[str]: A list of emails sent by the passed in sender.
        """
        logging.info("Getting emails from sender: {}".format(sender))
        
        emails = []
        for email in self.emails:
            email_sender = self.get_email_sender(email['id'])
            if sender == email_sender:
                emails.append(email)
        logging.info("Got {} emails from sender: {}".format(len(emails), sender))
        return emails

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deletes emails from the gmail account.")
    parser.add_argument('--top_n_senders', type=str, nargs='+', help='The email addresses of the senders to delete emails from.')
    parser.add_argument('--num_emails', type=int, default=4000, help='The number of emails to check through.')
    parser.add_argument('--progress_bar', type=bool, help='Whether or not to display a progress bar.')
    args = parser.parse_args()
    Deleter(
        senders=args.top_n_senders,
        num_emails=args.num_emails,
        progress_bar=args.progress_bar
    ).delete_emails()
        