import pytest
from gmail import GmailService
from google.oauth2.credentials import Credentials


@pytest.fixture
def gmail_service():
    return GmailService()


def test_gmail_service_init(gmail_service):
    assert gmail_service.credentials_path is not None


def test_gmail_service_get(gmail_service):
    assert gmail_service.get() is not None


def test_gmail_service_get_credentials(gmail_service):
    assert isinstance(gmail_service._get_credentials(), Credentials)
