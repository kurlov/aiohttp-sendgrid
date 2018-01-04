from sendgrid import Sendgrid


if __name__ == '__main__':
    import asyncio
    mailer = Sendgrid()
    loop = asyncio.get_event_loop()
    data = {'to': 'sasha-kurlov@ya.ru',
            'sender': 'sasha-kurlov@ya.ru',
            'subject': 'greetings',
            'content': '<h1>Hello</h1>'}
    loop.run_until_complete(mailer.send(**data))
