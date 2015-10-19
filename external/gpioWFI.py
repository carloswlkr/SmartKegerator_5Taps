import sys
import RPi.GPIO as GPIO

def leftFlowMeterTick(signal):
	print "Left beer tick!"
	sys.stdout.flush()

def centerLeftFlowMeterTick(signal):
	print "Center left beer tick!"
	sys.stdout.flush()

def centerFlowMeterTick(signal):
	print "Center beer tick!"
	sys.stdout.flush()

def centerRightFlowMeterTick(signal):
	print "Center right beer tick!"
	sys.stdout.flush()

def rightFlowMeterTick(signal):
	print "Right beer tick!"
	sys.stdout.flush()


def main(argv):
	if len(argv) != 5:
		print "Usage: gpioWFI flowMeter0Pin flowMeter1Pin flowMeter2Pin flowMeter3Pin flowMeter4Pin"
		return

	# get params
	leftPin = int(float(argv[0]))
	centerLeftPin = int(float(argv[1]))
	centerPin = int(float(argv[2]))
	centerRightPin = int(float(argv[3]))
	rightPin = int(float(argv[4]))

	# Setup GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(leftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(centerLeftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(centerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(centerRightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(rightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	GPIO.add_event_detect(leftPin, GPIO.RISING, callback=leftFlowMeterTick, bouncetime=20)
	GPIO.add_event_detect(centerLeftPin, GPIO.RISING, callback=centerLeftFlowMeterTick, bouncetime=20)
	GPIO.add_event_detect(centerPin, GPIO.RISING, callback=centerFlowMeterTick, bouncetime=20)
	GPIO.add_event_detect(centerRightPin, GPIO.RISING, callback=centerRightFlowMeterTick, bouncetime=20)
	GPIO.add_event_detect(rightPin, GPIO.RISING, callback=rightFlowMeterTick, bouncetime=20)
	
	try:
		raw_input()
	except KeyboardInterrupt:
		print "Keyboard interrupt!"
	except:
		print "Other interrupt!"
	finally:
		GPIO.cleanup()
		print "Cleaned up GPIO!"

	print "Exiting!"


if __name__ == "__main__":
	main(sys.argv[1:])