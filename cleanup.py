"""
This module implements the cleanup script. This script is used
to get a number of emails from your gmail account and .
"""

from collections import defaultdict
from rich.prompt import IntPrompt
from rich.theme import Theme
from rich.highlighter import RegexHighlighter
from rich.console import Console
from rich.prompt import Confirm
from typing import List
import pprint
import collections
import logging
import typer
import progressbar
from tabulate import tabulate
from gmail import GmailService
from models.email import Email


pp = pprint.PrettyPrinter(indent=4)

console = Console()


class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


def bytesto(bytes, to, bsize=1024):
    a = {"k": 1, "m": 2, "g": 3, "t": 4, "p": 5, "e": 6}
    r = float(bytes)
    return bytes / (bsize ** a[to])


def get_email_headers(email) -> dict:
    """
    Extracts the headers from the email and returns them as a dict.

    :param email: The email to extract the sender from.
    :return: The headers of the email.
    """
    headers = {"sender": "N/A", "subject": "N/A"}
    for header in email["payload"]["headers"]:
        if header["name"] == "From":
            headers["sender"] = header["value"]
        elif header["name"] == "Subject":
            headers["subject"] = header["value"]
    return headers


def print_emails(emails: list):
    """
    Prints the email info for emails in a list.

    :param emails: A list of emails to print.
    """
    counts = collections.Counter([email.subject for email in emails])
    size = bytesto(sum(email.size for email in emails), "m")
    for email in emails:
        console.print(f"{email.subject} - {email.sender} - {email.size} bytes")
    console.print(f"Total size: {size} MB")


class EmailFetcher:
    """
    This class fetches emails from the gmail account.

    :param num_emails: The number of emails to get.
    """

    def __init__(self):
        self.gmail = GmailService().get()

    def get_email_by_id(self, message_id, user: str = "me") -> dict:
        """
        Gets the email by the message id for specified user.

        :param message_id: The message to get the email for.
        :param user: The user to get the email for.
        """
        return self.gmail.users().messages().get(userId=user, id=message_id).execute()

    def parse_email(self, message) -> Email:
        """
        Parses the email and returns an Email object.

        :param message: The message to parse.
        :return: An Email object.
        """
        _email = self.get_email_by_id(message["id"])
        headers = get_email_headers(_email)
        return Email(
            id=_email["id"],
            size=_email["sizeEstimate"],
            sender=headers["sender"],
            subject=headers["subject"],
        )

    def extract_email_info(self, messages) -> list:
        """
        Extracts the needed information for emails in a response message.
        :param num_emails: The number of emails to get the senders for.
        :return: A list of emails.
        """
        emails = []
        for message in messages:
            _email = self.parse_email(message)
            emails.append(_email)
        return emails

    def get_response(self, token=None) -> list:
        """
        Gets the messages from the Gmail API for the logged in user.
        """
        return (
            self.gmail.users().messages().list(userId="me").execute()
            if token is None
            else self.gmail.users()
            .messages()
            .list(userId="me", pageToken=token)
            .execute()
        )

    def get(self, num_emails: int) -> list:
        """
        Gets a batch of messages from the Gmail class for the logged in user.
        """
        response = self.get_response()
        emails = []
        if len(response["messages"]) < num_emails and len(response["messages"]) < 100:
            console.print(
                f"{num_emails} requested but only {len(response['messages'])} emails found."
            )
        else:
            console.print(
                f"{len(response['messages'])} initially found. Attempting to fetch remaining {num_emails - len(response['messages'])} emails 100 at a time..."
            )
        num_requests = num_emails // len(response["messages"])
        for _ in progressbar.progressbar(range(num_requests)):
            emails.extend(self.extract_email_info(response["messages"]))
            if response.get("nextPageToken", None) is not None:
                response = self.get_response(response["nextPageToken"])
            else:
                break
        logging.info("Successfully retrieved %d messages", len(emails))
        return emails


class Deleter:
    """
    This class handles the deletion of emails. It takes in a list of emails, sorts them, and
    prompts the user about deletion.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the Deleter class.
        Args:
            kwargs (dict): A dictionary of keyword arguments.
                emails (List[str]): A list of Email objects to use for deletion.
        """
        logging.basicConfig(
            level=kwargs.get("log_level", logging.INFO),
            format="%(funcName)s():%(lineno)i: %(levelname)s: %(message)s",
        )
        self.gmail = GmailService().get()
        self.emails = kwargs.get("emails")

    def count_emails_by_sender(self) -> dict:
        """
        Loops through emails passed in to the class and creates a dict where
        the key is the sender and value is a list of emails associated with that sender.

        :return: A dict of emails grouped by sender.
        """
        emails_by_sender = defaultdict(list)
        for email in self.emails:
            emails_by_sender[email.sender].append(email)
        return emails_by_sender

    def _move_emails_to_trash(self, emails: List[Email]) -> None:
        """
        Moves the emails passed in to the trash of the gmail inbox.

        :param emails: A list of emails to move to the trash.
        """
        for email in emails:
            self.gmail.users().messages().trash(userId="me", id=email.id).execute()
        logging.info("Deleted %d emails.", len(emails))

    def run(self) -> None:
        """
        This method moves emails from the gmail account to trash.
        It groups the emails passed into the class by sender, then loops through senders in
        descending order by the email count in order to delete emails sent by that sender.

        """
        emails = self.count_emails_by_sender()
        senders = sorted(emails, key=lambda k: len(emails[k]), reverse=True)
        table = [[sender, len(emails[sender])] for sender in senders]
        theme = Theme({"example.email": "bold magenta"})
        console = Console(highlighter=EmailHighlighter(), theme=theme)
        console.print(tabulate(table, headers=["Sender", "Count"]))
        for sender in senders:
            num_emails = len(emails[sender])
            answer = Confirm.ask(
                f"View more info on {num_emails} emails from {sender}?"
            )
            if answer:
                print_emails(emails[sender])
            answer = Confirm.ask(f"Delete all {num_emails} emails from {sender}?")
            if answer.lower() == "y":
                logging.info("Deleting emails from sender: %s", sender)
                self._move_emails_to_trash(emails[sender])


def main():
    """
    Get the number of emails, count the amount of emails per sender, and delete the emails from
    the top senders.
    """
    option = IntPrompt.ask("Enter the number of emails to delete")
    emails = EmailFetcher().get(option)
    Deleter(emails=emails).run()


if __name__ == "__main__":
    typer.run(main())
