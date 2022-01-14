from rich.prompt import IntPrompt, Prompt
from rich.theme import Theme
from rich.highlighter import RegexHighlighter
from rich.console import Console
from rich.pretty import pprint
from rich.prompt import Confirm
from rich.text import Text
from cleanup import EmailFetcher, Deleter

import typer

app = typer.Typer()

console = Console()


def send_email():
    raise NotImplementedError


def analyze_emails():
    raise NotImplementedError


def archive_emails():
    option = IntPrompt.ask("Enter the number of emails to fetch:", default=1000)
    emails = EmailFetcher().get(option)
    pprint(emails)
    Deleter(emails=emails).run()


def label_emails():
    raise NotImplementedError


def main():
    """
    Get the number of emails, count the amount of emails per sender, and delete the emails from
    the top senders.
    """
    action = Prompt.ask(
        "What would you like to do?",
        choices=["send_email", "analyze_emails", "archive_emails", "label_emails"],
        default="analyze_emails",
    )
    if action == "send_email":
        send_email()
    elif action == "analyze_emails":
        analyze_emails()
    elif action == "archive_emails":
        archive_emails()
    elif action == "label_emails":
        label_emails()
    else:
        raise ValueError(f"Unknown action: {action}")


if __name__ == "__main__":
    main()
