import aiohttp
import asyncio
import os


API_KEY = os.environ.get('SENDGRID_API_KEY')
API_URL = 'https://api.sendgrid.com/v3/mail/send'
auth = 'Bearer ' + str(API_KEY)
headers = {'content-type': 'application/json', 'authorization': auth}
loop = asyncio.get_event_loop()

async def fetch(session, url, payload):
    async with session.post(url, data=payload, headers=headers) as response:
        return await response.json()

async def send(payload):
    async with aiohttp.ClientSession(loop=loop) as session:
        response = await fetch(session, API_URL, payload)
        print(response)

if __name__ == '__main__':
    data = {"personalizations": [
    {
      "to": [
        {
          "email": "sasha-kurlov@ya.ru",
          "name": "Sasha"
        }
      ],
      "subject": "Hello, World!"
    }
  ],
  "from": {
    "email": "sam.smith@example.com",
    "name": "Sam Smith"
  },
  "subject": "Hello, World!",
  "content": [
    {
      "type": "text/html",
      "value": "<html><p>Hello, world!</p></html>"
    }
  ]
}
    loop.run_until_complete(send(data))
