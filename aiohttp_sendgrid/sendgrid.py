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
            Example::

            mailer = Sendgrid()
            # to might be heterogeneous
            to = ['name@example.com', {'email': 'name2@example.com'},
                  {'email': 'name3example.com', 'name': 'Name3'}]
            # also might be a dictionary with ``email``and ``name`` keys
            sender = 'from.me@example.com'
            subject = 'greetings'
            # default mime type is ``text/html``
            content = '<h1>Hello, world</h1>'
            mailer.send(to, sender, subject, content)

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

            # TODO: add cc, bcc, reply_to support
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
        """Helper coroutine to fetch post requests via ``aiohttp.ClientSession``

            :param session: a ``aiohttp.ClientSession`` object
            :param url: a string with url to fetch
            :param payload: a dictionary which will be passed as JSON for POST
        """
        async with session.post(url, json=payload, headers=self.headers) as r:
            if r.status == 202:
                return await r.text()
            else:
                return await r.json()

    @staticmethod
    def _generate_email(email, name=None):
        """Helper to convert values into email dictionary.

            :param email: a string with email address
            :param name: (optional) a string with recipient's name
            :return dictionary object
        """
        result = {'email': email}
        if name:
            result['name'] = name
        return result

    def _parse_to_emails(self, to_emails):
        """Helper which helps to parse recipient(s) information.

            Example of valid input::

            'name@example.com'
            {'email': 'name@example.com'}
            {'email': 'name@example.com', 'name': 'Name'}
            ['name@example.com']
            ['name@example.com', 'name2@example.com']
            [{'email': 'name@example.com'}]
            [{'email': 'name@example.com'}, {'email': 'name2@example.com'}]
            [{'email': 'name@example.com', 'name': 'Name'}]
            [{'email': 'name@example.com', 'name': 'Name'},
             {'email': 'name2@example.com', 'name': 'Name2'}]
            ['name@example.com', {'email': 'name2@example.com'},
             {'email': 'name3@example.com', 'name': 'Name3'}]

            :param to_emails: might be a string of dictionary with ``email``
                              key, ``name`` key is optional. Also might be a
                              list or tuple with appropriate strings or
                              dictionaries
        """
        tos = []
        if not isinstance(to_emails, (list, tuple)):
            to_emails = [to_emails]
        for email in to_emails:
            if isinstance(email, str):
                tos.append(self._generate_email(email))
            elif isinstance(email, dict):
                tos.append(self._generate_email(**email))
            else:
                raise ValueError('Invalid data format')
        return tos

    def _parse_from_email(self, from_email):
        """Helper for parsing sender's email.

            :param from_email: might be a string or dictionary with ``email``
                               key, ``name`` key is optional
        """
        if isinstance(from_email, str):
            return self._generate_email(from_email)
        elif isinstance(from_email, dict):
            return self._generate_email(**from_email)
        else:
            raise ValueError('Invalid from email adress')
