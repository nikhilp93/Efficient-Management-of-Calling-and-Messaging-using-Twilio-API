from twilio.rest import TwilioRestClient
from twilio import twiml
from datetime import date

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACf0757674cd3d5092237f0ee7afca722e"
AUTH_TOKEN = "0262869362eb19211cb4a85d215440a6"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body=input('Enter message to be sent\n'),  # Message body, if any #input('Enter message to be sent\n')
    to=input('Enter your phone number\n'),
    from_="+13023856046",
    media_url="http://www.hdwallpapers.in/walls/pawan_kalyan-wide.jpg"
)

'''
media_url=[  # List of media URLs, if any
        "http://example.com/image1.jpg",
        "http://example.com/image2.jpg",

'''
print(message.sid)

for message in client.messages.list():
    print(message.body)

messages = client.messages.list(
    to="+16692261830",
    date_sent=date(2015,4,18),
)
#input('Enter the phone number\n'),"+16692261830","+13015260890"

for message in messages:
    print(message.body)

'''

Redacting or Deleting Message Records

To protect your users’ privacy and/or comply with legal requirements, Twilio allows you to redact your Message bodies or delete the records outright.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
message_sid = "MM123"

client.messages.redact(message_sid)
message = client.messages.get(message_sid)
print message.body  # Will be an empty string

client.messages.delete(message_sid)  # Deletes record entirely, subsequent requests will return 404

'''
