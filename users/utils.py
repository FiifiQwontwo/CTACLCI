import os
from twilio.rest import Client

account_sid = 'AC9d1a78bae11c1fbd7f948bf4f1db8447'
auth_token = 'f5cc6bf6d116231e35bec177d7925a63'
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
                              body=f'HI! Your verification code is {user_code}',
                              from_='+16784987342',
                              to=f'{phone_number}'
                             )

    print(message.sid)
