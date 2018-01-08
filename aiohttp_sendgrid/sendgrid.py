import aiohttp
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
            tos = {'to': self._parse_to_emails(to)}
            send_from = self._parse_from_email(sender)
            body = [{'type': body_type, 'value': content}]
            payload['personalizations'].append(tos)
            payload['from'] = send_from
            payload['subject'] = subject
            payload['content'] = body
            return payload
        url = SENDGRID_API_URL + SEND_URN
        payload = generate_payload()
        async with aiohttp.ClientSession() as session:
            response = await self._post(session, url, payload)
            return response

    async def _post(self, session, url, payload):
        async with session.post(url, json=payload, headers=self.headers) as r:
            if r.status == 202:
                return await r.text()
            else:
                return await r.json()

    @staticmethod
    def _generate_email(self, email, name=None):
        result = {'email': email}
        if name:
            result['name'] = name
        return result

    @staticmethod
    def _parse_to_emails(self, to_emails):
        tos = []
        if isinstance(to_emails, str):
            tos.append(self._generate_email(to_emails))
        elif isinstance(to_emails, dict):
            tos.append(self._generate_email(**to_emails))
        elif isinstance(to_emails, (list, tuple, set)):
            for email in to_emails:
                if isinstance(email, str):
                    tos.append(self._generate_email(email))
                elif isinstance(email, dict):
                    tos.append(self._generate_email(**email))
                else:
                    raise ValueError('Invalid to email address')
        else:
            raise ValueError('Invalid to email address')
        return tos

    @staticmethod
    def _parse_from_email(self, from_email):
        if isinstance(from_email, str):
            return self._generate_email(from_email)
        elif isinstance(from_email, dict):
            return self._generate_email(**from_email)
        else:
            raise ValueError('Invalid from email adress')
