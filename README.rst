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

Usage
-----
Create an instance of API client:

.. code:: python

    import asyncio
    from aiohttp_sendgrid import Sendgrid
    api_key = '<your_sendgrid_api_key>'
    mailer = Sendgrid(api_key=api_key)

Important to note that if ``api_key`` is not provided then it will try to
read ``SENDGRID_API_KEY`` environment variable

Send email to single recipient
-------------------------------
.. code:: python

    to = 'to@example.com'
    sender = 'from@example.com'
    subject = 'greetings'
    content = '<h1>Hello</h1>'
    send_mail = mailer.send(to, sender, subject, content)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_mail)

Both ``to`` and ``sender`` might be also a dictionary with ``email`` key,
if you want to specify name for sender or recipient then add ``name`` key to
the dictionary. Thus, ``to = {'email': 'to@example.com', 'name': 'Recipient'}``
is also a correct value.

Send single email to multiple recipients
----------------------------------------
.. code:: python

    to = ['to@example.com', 'another@example']
    sender = 'from@example.com'
    subject = 'greetings'
    content = '<h1>Hello</h1>'
    send_mail = mailer.send(to, sender, subject, content)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_mail)

``to`` might be tuple or list of strings or dictionaries.
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

Development
-----------
``pip install -r requirements.dev.txt``

