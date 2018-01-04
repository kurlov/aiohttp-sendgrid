import aiohttp
import asyncio
import os

SENDGRID_API_URL = 'https://api.sendgrid.com/v3'
SEND_URN = '/mail/send'


class Sendgrid(object):
    """Wrapper around sendgrid v3 API. """

    def __init__(self, api_key=None):
        """Create wrapper instance

        if non Sendgrid API key provided, get it from env variable
        """
        self.api_key = api_key
        if not api_key:
            self.api_key = os.environ.get('SENDGRID_API_KEY')
        if not self.api_key:
            raise ValueError('No API key provided')
        auth = 'Bearer ' + str(self.api_key)
        self.headers = {'authorization': auth}

    async def send(self, to, sender, subject, content, body_type='text/html'):
        def generate_payload():
            payload = {'personalizations': []}
            tos = {'to': [{'email': to}]}
            send_from = {"email": sender}
            body = [{'type': body_type, 'value': content}]
            payload['personalizations'].append(tos)
            payload['from'] = send_from
            payload['subject'] = 'subject'
            payload['content'] = body
            return payload
        url = SENDGRID_API_URL + SEND_URN
        payload = generate_payload()
        async with aiohttp.ClientSession() as session:
            response = await self._post(session, url, payload)
            print(response)

    async def _post(self, session, url, payload):
        async with session.post(url, json=payload, headers=self.headers) as r:
            if r.status == 202:
                return await r.text()
            else:
                return await r.json()
