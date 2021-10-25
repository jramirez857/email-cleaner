"""
This module implements the GmailSenders class. This class is used to
get the list of senders from a Gmail account for a given number of emails.
"""

from collections import defaultdict, OrderedDict
import pprint
import json
import logging
import progressbar
import argparse
from itertools import islice
from gmail import Gmail


pp = pprint.PrettyPrinter(indent=4)


class EmailParser:
    """
    This class is used to get the list of senders for a given number of emails.

    :param num_emails: The number of emails to get the senders for.
    :param gmail_service: The Gmail API service.
    :param log_level: The logging level.
    :var senders: An OrderedDict of senders and their counts in descending order.

    """

    def __init__(self, **kwargs):
        self.num_emails = kwargs.get("num_emails", 100)
        self.gmail = kwargs.get("gmail_service", Gmail().service)
        logging.basicConfig(
            level=kwargs.get("log_level", logging.INFO),
            format="%(funcName)s():%(lineno)i: %(levelname)s: %(message)s",
        )
        self.senders = self.get_ordered_senders()

    def __str__(self):
        return pp.pformat(self.senders)

    def __repr__(self) -> str:
        return f"ExtractSenders(num_emails={self.num_emails},\n senders={self.senders})"

    def get_num_messages(self, user_id="me") -> list:
        """
        Gets a batch of messages from the Gmail class for the logged in user.
        """
        response = self.gmail.users().messages().list(userId=user_id).execute()
        messages = []
        while response.get("nextPageToken", None) and len(messages) < self.num_emails:
            for message in response["messages"]:
                messages.append(message)
            response = (
                self.gmail.users()
                .messages()
                .list(userId=user_id, pageToken=response["nextPageToken"])
                .execute()
            )
            logging.debug(
                "Successfully retrieved %d messages", len(response["messages"])
            )
        logging.info("Successfully retrieved %d messages", len(messages))
        return messages

    def get_sender(self, email) -> str:
        """
        Extracts the sender from the email and adds it to the senders dictionary.
        Increments the count for the sender in the dictionary.

        :param email: The email to extract the sender from.
        :return: The sender of the email.
        """
        logging.debug(
            "headers_type: %s",
            type(email["payload"]["headers"]),
            "headers: %s",
            email["payload"]["headers"],
        )
        sender = "Unknown Sender"
        for header in email["payload"]["headers"]:
            if header["name"] == "From":
                sender = header["value"]
                break
        return sender

    def get_email_by_id(self, message_id, user="me") -> dict:
        """
        Gets the email by the message id for specified user.

        :param message: The message to get the email for.
        """
        return self.gmail.users().messages().get(userId="me", id=message_id).execute()

    def get_ordered_senders(self) -> OrderedDict:
        """
        Gets a list of senders from the Gmail API for the logged in user.

        :return: An OrderedDict of senders and their counts in descending order.

        """
        senders = defaultdict(int)
        messages = self.get_num_messages()
        for i, message in zip(progressbar.progressbar(messages), messages):
            email = self.get_email_by_id(message["id"])
            senders[self.get_sender(email)] += 1
            logging.debug("senders is size: %d and type: ", len(senders))
        logging.info("Got %d senders from %d messages", len(senders), len(messages))
        ordered_senders = OrderedDict(sorted(senders.items(), key=lambda x: x[1], reverse=True))
        logging.info("Your top 10 email senders in your last %d emails are: ", len(messages))
        pp.pprint(list(islice(ordered_senders, 10))[:10])
        return dict(ordered_senders)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get the senders for a given number of emails."
    )
    parser.add_argument(
        "-n",
        "--num_emails",
        type=int,
        default=100,
        help="The number of emails to get the senders for.",
    )
    args = parser.parse_args()
    emails = EmailParser(log_level=logging.INFO, num_emails=args.num_emails)
    with open("senders.json", "w") as f:
        f.write(json.dumps(emails.senders, indent=4))
