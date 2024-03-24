#import module for raspberry pi gpio 
import RPi.GPIO as GPIO
#import module for time
import time

#if time is 10am 
if time.strftime("%H") == "10":
    #set the gpio mode to board
    GPIO.setmode(GPIO.BOARD)
    #set the gpio pin 7 to output
    GPIO.setup(7, GPIO.OUT)
    #turn on the motor
    GPIO.output(7, True)
    #wait for 1 second
    time.sleep(0.2)
    #turn off the motor
    GPIO.output(7, False)
    #clean up the gpio
    GPIO.cleanup()
