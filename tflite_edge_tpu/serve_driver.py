import RPi.GPIO as GPIO
import time

def setAngle(angle):
	duty = angle / 18 + 2
	return duty

def move_servo(x0):
	servoPIN = 17
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servoPIN, GPIO.OUT)
	p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
	p.start(2.5) # Initialization
	p.ChangeDutyCycle(5)
	time.sleep(0.5)
	angle = (x0 * 180)/600
	duty = setAngle(angle)
	p.ChangeDutyCycle(duty)
	time.sleep(0.5)
	p.stop()
	GPIO.cleanup()
