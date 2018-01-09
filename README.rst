aiohttp-sendgrid
================
.. image:: https://travis-ci.org/Kurlov/aiohttp-sendgrid.svg?branch=master
    :target: https://travis-ci.org/Kurlov/aiohttp-sendgrid
.. image:: https://badge.fury.io/py/aiohttp-sendgrid.svg
    :target: https://badge.fury.io/py/aiohttp-sendgrid
SendGrid mail API wrapper

Installation
------------
``pip install aiohttp_sendgrid``

Send email to single recipient
-------------------------------
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

Send single email to multiple recipients
----------------------------------------
.. code:: python

    import asyncio
    from aiohttp_sendgrid import Sendgrid
    mailer = Sendgrid()
    to = ['to@example.com', 'another@example']
    sender = 'from@example.com'
    subject = 'greetings'
    content = '<h1>Hello</h1>'
    send_mail = mailer.send(to, sender, subject, content)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_mail)
