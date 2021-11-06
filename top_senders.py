"""
This module implements the GmailSenders class. This class is used to
get the list of senders from a Gmail account for a given number of emails.
"""

from collections import defaultdict, OrderedDict
import pprint
import logging
import argparse
import progressbar
from gmail import GmailService
from models.email import Email


pp = pprint.PrettyPrinter(indent=4)


class TopSenders:
    """
    This class is used to get the list of senders for a given number of emails.

    :param num_emails: The number of emails to get the senders for.
    :param gmail_service: The Gmail API service.
    :param log_level: The logging level.
    :var senders: An OrderedDict of senders and their counts in descending order.

    """

    def __init__(self, **kwargs):
        self.gmail = kwargs.get("gmail_service", GmailService().get())
        logging.basicConfig(
            level=kwargs.get("log_level", logging.DEBUG),
            format="%(funcName)s():%(lineno)i: %(levelname)s: %(message)s",
        )

    def _parse_email(self, message) -> Email:
        """
        Parses the email and returns an Email object.

        :param message: The message to parse.
        :return: An Email object.
        """
        _email = self.get_email_by_id(message["id"])
        _sender = self._get_sender(_email)
        return Email(id=_email["id"], sender=_sender)

    def _extract_email_info(self, messages: list) -> list:
        """
        Extracts the needed information for emails in a response message.

        :param num_emails: The number of emails to get the senders for.
        :return: A list of emails.

        """
        emails = []
        for message in messages:
            _email = self._parse_email(message)
            emails.append(_email)
        return emails

    def _get_response(self, token=None) -> list:
        """
        Gets the messages from the Gmail API for the logged in user.
        """
        return (
            self.gmail.users().messages().list(userId="me", pageToken=token).execute()
            if token
            else self.gmail.users().messages().list(userId="me").execute()
        )

    def _get_num_emails(self, num: int) -> list:
        """
        Gets a batch of messages from the Gmail class for the logged in user.
        """
        response = self._get_response()
        emails = []
        logging.info("Getting %d emails", num)
        for _ in progressbar.progressbar(range(0, num, len(response["messages"]))):
            messages = response["messages"]
            emails.extend(self._extract_email_info(messages))
            if response.get("nextPageToken", None) is not None:
                response = self._get_response(response["nextPageToken"])
            else:
                logging.warning("No more messages")
                break
        logging.info("Successfully retrieved %d messages", len(emails))
        return emails

    def _get_sender(self, email) -> str:
        """
        Extracts the sender from the email and adds it to the senders dictionary.
        Increments the count for the sender in the dictionary.

        :param email: The email to extract the sender from.
        :return: The sender of the email.
        """
        sender = "Unknown Sender"
        for header in email["payload"]["headers"]:
            if header["name"] == "From":
                sender = header["value"]
                break
        return sender

    def get_email_by_id(self, message_id, user="me") -> dict:
        """
        Gets the email by the message id for specified user.

        :param message_id: The message to get the email for.
        :param user: The user to get the email for.
        """
        return self.gmail.users().messages().get(userId=user, id=message_id).execute()

    def get(self, num_emails: int, num_senders: int = 10) -> OrderedDict:
        """
        Gets a list of top senders from the Gmail API for the logged in user.

        :param num_emails: The number of emails to get the senders for.
        :param num_senders: The number of senders to return.
        :return: A list of the top senders of size num_senders.

        """
        senders = defaultdict(int)
        emails = self._get_num_emails(num=num_emails)
        logging.info(f"Getting top senders for { len(emails) } number of emails.")
        for email in progressbar.progressbar(emails):
            senders[email.sender] += 1
        top_senders = sorted(senders, key=senders.get, reverse=True)[:num_senders]
        logging.info("top senders: %s", top_senders)
        return top_senders


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get the senders for a given number of emails."
    )
    parser.add_argument(
        "-n",
        "--num_emails",
        type=int,
        default=1000,
        help="The number of emails to get the senders for.",
    )
    args = parser.parse_args()
    top_senders = TopSenders(log_level=logging.INFO).get(num_emails=args.num_emails)
    pp.pprint(top_senders)
