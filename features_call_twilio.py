'''Phone Calls

The Calls resource manages all interaction with Twilio phone calls, including the creation and termination of phone calls. For more information, see the Calls REST Resource documentation.
Making a Phone Call

The Calls resource allows you to make outgoing calls. Before a call can be successfully started, you’ll need a to set up a url endpoint which outputs valid TwiML. This can be done with the :class: twiml.Response class, get started here.


'''

from twilio.rest import TwilioRestClient
# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACf0757674cd3d5092237f0ee7afca722e"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
call = client.calls.create(to=input('Enter your phone number\n'), from_="+13023856046",
                           url="http://foo.com/call.xml")
#print(call.length)
print(call.sid)


'''
Retrieve a Call Record

If you already have a Call sid, you can use the client to retrieve that record.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
'''
#sid = "ACf0757674cd3d5092237f0ee7afca722e"
#call = client.calls.get(sid)

'''

Delete a Call Record

You can delete your Call resources from Twilio’s storage to protect your users’ privacy and/or comply with legal requirements.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
sid = "CA12341234"
client.calls.delete(sid)

Accessing Specific Call Resources

Each Call resource also has access to its notifications, recordings, and transcriptions. These attributes are ListResources, just like the Calls resource itself.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
sid = "CA12341234"
call = client.calls.get(sid)

print call.notifications.list()
print call.recordings.list()
print call.transcriptions.list()

However, what if you only have a call_sid, and not the actual Resource? No worries, as Calls.list() can be filtered based on a given call_sid.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
sid = "CA24234"
print client.notifications.list(call=sid)
print client.recordings.list(call=sid)
print client.transcriptions.list(call=sid)

Modifying Live Calls

The Call resource makes it easy to find current live calls and redirect them as necessary

from twilio.rest import TwilioRestClient
from twilio.rest.resources import Call

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
calls = client.calls.list(status=Call.IN_PROGRESS)
for c in calls:
    c.route(
        "http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
        method="POST"
    )

Ending all live calls is also possible

from twilio.rest import TwilioRestClient
from twilio.rest.resources import Call

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
calls = client.calls.list(status=Call.IN_PROGRESS)
for c in calls:
    c.hangup()

Note that hangup() will also cancel calls currently queued.

If you already have a Call sid, you can use the Calls resource to update the record without having to use get() first.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
sid = "CA12341234"
client.calls.update(sid, method="POST",
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

Hanging up the call also works.

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
sid = "CA12341234"
client.calls.hangup(sid)

'''
