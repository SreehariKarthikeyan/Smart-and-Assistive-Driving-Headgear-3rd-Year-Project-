import urllib 
def sendSMS(uname, pword, numbers, sender, message): 
  params = {'uname':uname, 'pword':pword, 'selectednums':numbers, 'message':message, 'from':sender}
  f = urllib.urlopen('https://www.textlocal.co.uk/sendsmspost.php?' + urllib.urlencode(params))
  return (f.read(), f.code)

#Send sms driver And within the if statement block where motion is detected, alter it so it reads:

if Current_State==1 and Previous_State==0: print " Motion detected!" sendSMS("jasebell@xxxxxxxx", "xx_password_xx", "447900xxxxxxx", "4479"


#Main.py

import RPi.GPIO as GPIO
import time
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_VIB = 7
print "PIR Module Test (CTRL-C to exit)"
# Set pin as input
GPIO.setup(GPIO_VIB,GPIO.IN)      # Echo


Current_State  = 0
Previous_State = 0

try:
while GPIO.input(GPIO_VIB)==1:
    Current_State  = 0
  print "  Ready"
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_VIB)
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
    # Wait for 10 milliseconds
    time.sleep(0.01)
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings

  GPIO.cleanup()
