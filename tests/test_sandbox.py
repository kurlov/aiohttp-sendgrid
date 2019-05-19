from unittest.mock import Mock

from aiohttp_sendgrid import Sendgrid
import pytest

pytestmark = pytest.mark.asyncio


@pytest.fixture
def sendgrid():
    sg = Sendgrid(api_key="blah")

    async def mock_post(_, __, payload):
        return payload

    sg._post = mock_post
    return sg


async def test_sandbox(sendgrid):

    payload = await sendgrid.send("to@example.com", "from@example.com", "mysubject", "mycontent", sandbox=True)

    assert payload["mail_settings"]["sandbox_mode"]["enable"] is True


async def test_no_sandbox(sendgrid):

    payload = await sendgrid.send("to@example.com", "from@example.com", "mysubject", "mycontent")

    assert "mail_settings" not in payload
