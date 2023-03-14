# /etc/init.d/sample.py
### BEGIN INIT INFO
# Provides:          sample.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
import serial
import time
for x in range(15):
  try:
    ser = serial.Serial(f"COM{x}")
    print(f"COM{x}")
  except:
    pass
#import RPi.GPIO as io
print("starting the log")
with open("log.txt","a") as file:
  while True:
    data = ser.read()
    if len(data) > 0:
      file.write(data)
