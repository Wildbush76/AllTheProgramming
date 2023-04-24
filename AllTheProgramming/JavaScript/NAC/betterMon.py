import subprocess
from twilio.rest import Client
import pathlib

account_sid = 'yea2'
auth_token = 'yea'
print("Starting")


client = Client(account_sid, auth_token)
f_name = pathlib.Path('chat.html')

lastModfied = 0

message = client.messages.create(
    from_='+12183079973', body='System Online', to='+13615639161')

while True:
    # popen = subprocess.Popen(["powershell.exe", f"Get-Content {file} -tail 0 -wait"],stdout=subprocess.PIPE, universal_newlines=True)
    popen = subprocess.run(
        ["tail", "-f", "chat.html"], stdout=subprocess.PIPE, universal_newlines=True)
    for s in iter(popen.stdout.readline, ""):
        for line in s.strip().split("\n"):
            print(f"got a new line nerd {line}")
            if "m " in line and "Server" in line:
                message = client.messages.create(
                    from_='+12183079973', body='The nerd is here', to='+13615639161')
