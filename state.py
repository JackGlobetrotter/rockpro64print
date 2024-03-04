import sys
import RP64.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

var_gpio_in = 15

GPIO.setmode(GPIO.BOARD)
sys.exit(int(GPIO.input(var_gpio_in)))                    # Return state of GPIO
