import RP64.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
var_gpio_out = 13

GPIO.setmode(GPIO.BOARD)


GPIO.output(var_gpio_out, GPIO.HIGH)                         # Set GPIO to LOW

sleep(.5)

GPIO.output(var_gpio_out, GPIO.LOW)
