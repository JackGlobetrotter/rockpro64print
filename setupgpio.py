import RP64.GPIO as GPIO
from time import sleep
import subprocess

GPIO.setwarnings(False)
var_gpio_out = 13
var_gpio_in = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(var_gpio_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(var_gpio_in, GPIO.IN)

subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/class/gpio"])
subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/devices/platform/pinctrl/ff730000.gpio1"])
subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/devices/platform/pinctrl/ff780000.gpio2"])
subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/devices/platform/pinctrl/ff788000.gpio3"])
subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/devices/platform/pinctrl/ff790000.gpio4"])
subprocess.run(["/usr/bin/chown","-R","root:gpio","/sys/devices/platform/pinctrl/ff720000.gpio0"])
