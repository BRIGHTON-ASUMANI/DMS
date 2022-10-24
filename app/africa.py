# import package
import africastalking
from django.shortcuts import redirect
from . gateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from .models import Event
from multiprocessing import Process
import schedule
import time

import datetime as dt

def sms(request):
    print('smsing')
    phones = []
    event = Event.objects.all()
    for x in event:
        if x.user.profile.phone_number:
            numbers = x.user.profile.phone_number
            message = x.notes
            print(numbers)
            phones.append(numbers)
    # Initialize SDK
    username = "brighton"    # use 'sandbox' for development in the test environment
    api_key = "18696560f647f921b072950f4ef9e5c24a76e583ec26b6ceb4f2ef6d34403daabb"      # use your sandbox app API key for development in the test environment
    africastalking.initialize(username, api_key)


    # Initialize a service e.g. SMS
    sms = africastalking.SMS


    # Use the service synchronously
    response = sms.send(message, phones)
    print(response)

    # Or use it asynchronously
    def on_finish(error, response):
        if error is not None:
            raise error
        print(response)
    #
    # sms.send("Hello Message!", ["+2547xxxxxx"], callback=on_finish)
    return redirect('home')

def waiter():
    while  True:
        print('xxs')
        now = dt.datetime.now().strftime('%H:%M:%S')
        event = Event.objects.all()
        for x in event:
            print('vbnmk')
            print(x.start_time)
            if  str(x.start_time) == now :
                sms(x)
                print('matd6f7yughiojopjihgf;vcjihuyi ukvfkjdbcknxvb bfidukhcvx oifvdkjchvoufedkjchvouefvdkjhcvo fekjdchvbiu kjfhdcbvi hjfgdvbv ijhfdhbui fkdjhbcv nuifkdjhb nifdkjhckv nufidkjchb nifdkjcmbyftduyiuhgf7tuygched')
                continue    
            else:
                print('badoedrftgyhujikolp;['']')

        print('noma ')
        continue

Process(target=waiter).start()
