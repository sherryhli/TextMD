from twilio.rest import Client
from twilio import twiml
from twilio.rest import TwilioRestClient
import secrets

account_sid = secrets.TWILIO_ACCOUNT_SID
auth_token = secrets.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

client.messages.create(
        to = secrets.TWILIO_RECEIVER,
        from_ = secrets.TWILIO_SENDER,
        #Example of mass message to send 
        body= "Hey there!",
    )