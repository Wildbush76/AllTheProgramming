import time
from twilio.rest import Client
import pathlib

account_sid = 'AC127f608fa1d159909108f1f27bd94609'
auth_token = '4482486b8386d9c898e839bc17a1f13b'
print("Starting")


client = Client(account_sid, auth_token)
f_name = pathlib.Path('chat.html')

lastModfied = 0

message = client.messages.create(
    from_='+12183079973', body='System Online', to='+13615639161')

while True:
    try:
        newModified = f_name.stat().st_mtime
        if lastModfied != newModified:
            lastModfied = newModified
            with open("chat.html", "r") as file:
                chat = file.read().strip().split("\n")
                if "Server ->" in chat[-1] and " m " in chat[-1]:
                    message = client.messages.create(
                        from_='+12183079973', body='they have joined', to='+13615639161')
    except Exception as e:
        print(e)
    finally:
        time.sleep(30)
