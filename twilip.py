import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='PRIORITYHEALTH- Reminder to exercise for 1hour today. There are many ways you can do that. See priorityhealth.tech for more info.',
                              from_='+15017122661',
                              to='+15558675310'
                          )

print(message.sid)
