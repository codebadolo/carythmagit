from django.shortcuts import render
from twilio.base.exceptions import TwilioRestException
# Create your views here. 
from twilio.rest import Client
from django.conf import settings                                                                                                                                                      
from django.http import HttpResponse
 
#from twilio.rest import TwilioRestClien

# Create your views here.

'''
MY_ACCOUNT_SID = "AC4f4516dd1894fa8d162842e79ae660d1"
TWILIO_AUTH_TOKEN="72017c407c0c855f9d7cdc7377f7528f"
MY_TWILIO_NUMBER="+16187871636"

'''

#723786
"""
TWILIO_ACCOUNT_SID = 'AC4f4516dd1894fa8d162842e79ae660d1'
TWILIO_AUTH_TOKEN = '72017c407c0c855f9d7cdc7377f7528f'
TWILIO_NUMBER = "+16187871636" 
"""

  
def broadcast_sms(request):
    message_to_broadcast = ("How are you")
    client = Client(settings.TWILIO_ACCOUNT_SID , settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
    #recipient =   "+22661396930"
        try: 

        #print(recipient)
            if recipient:
                client.messages.create(to=recipient,from_= settings.TWILIO_NUMBER,body=message_to_broadcast)
                return HttpResponse("messages sent!" + message_to_broadcast)
        except TwilioRestException as e:
            print(e)
                #return " the  message  is not sent  "





