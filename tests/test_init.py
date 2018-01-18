from aiohttp_sendgrid import Sendgrid
import pytest
import os


@pytest.fixture
def mailer():
    mailer = Sendgrid()
    return mailer


def test_api_key_from_env(mailer):
    m = mailer
    assert isinstance(m.api_key, str) is True
