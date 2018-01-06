aiohttp-sendgrid
================
SendGrid Web API v3 aiohttp wrapper

Basic Usage
-----------
.. code:: python

    import asyncio
    from aiohttp_sendgrid import Sendgrid
    mailer = Sendgrid()
    to = 'to@example.com'
    sender = 'from@example.com'
    subject = 'greetings'
    content = '<h1>Hello</h1>'
    send_mail = mailer.send(to, sender, subject, content)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_mail)
