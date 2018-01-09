import aiohttp
import os

SENDGRID_API_URL = 'https://api.sendgrid.com/v3'
SEND_URN = '/mail/send'


class Sendgrid(object):
    """This class performs requests to sendgrid Mail Send v3 API.

    More detailed information about Mail Send endpoint might be found here:
    https://sendgrid.com/docs/API_Reference/api_v3.html

    :param api_key: A string with sendgrid API key, if not provided
                    ``SENDGRID_API_KEY`` environment variable will be used.
                    You can manage your API keys
                    in settings -> API keys in your sendgrid account.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key
        if not api_key:
            self.api_key = os.environ.get('SENDGRID_API_KEY')
        if not self.api_key:
            raise ValueError('No API key provided')
        auth = 'Bearer ' + str(self.api_key)
        self.headers = {'authorization': auth}

    async def send(self, to, sender, subject, content, body_type='text/html'):
        """This coroutine performs ``/mail/send`` POST requests via ``aiohttp``

            :param to: Might be a ``string`` with email address or dictionary
                       with ``email`` key, ``name``(optional). Also
                       might be list or tuple of strings or dictionaries.
                       Both list and tuple might be heterogeneous,
                       it is okey to put strigns and dictionaries together.
                       This parameters specifies email recipient(s)
            :param sender: Might be a ``string`` with email address or
                           dictionary with ``email`` key, ``name``(optional).
                           Specifies from which address email(s) will be sent.
            :param subject: A string with email subject
            :param content: A string which contains actual content of email.
                            It depends on ``body_type`` how it will be viewed.
            :param body_type: (optional) a string which specifies mime type
                              of the content.
                              By default it equals to ``text/html``.
                              Might be ``text/html`` or ``text/plain``
        """
        def generate_payload():
            """Closure to aplly parse functions on input data: ``to``, ``sender``
            """
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
    def _generate_email(email, name=None):
        result = {'email': email}
        if name:
            result['name'] = name
        return result

    def _parse_to_emails(self, to_emails):
        tos = []
        if isinstance(to_emails, str):
            tos.append(self._generate_email(to_emails))
        elif isinstance(to_emails, dict):
            tos.append(self._generate_email(**to_emails))
        elif isinstance(to_emails, (list, tuple)):
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

    def _parse_from_email(self, from_email):
        if isinstance(from_email, str):
            return self._generate_email(from_email)
        elif isinstance(from_email, dict):
            return self._generate_email(**from_email)
        else:
            raise ValueError('Invalid from email adress')
