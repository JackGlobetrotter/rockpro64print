# Enable UART4 in `armbian-config`

#install Python3 and Pip3




#gpio

sudo pip3 install git+https://github.com/Angoosh/RockPro64-RP64.GPIO

groupadd gpio
usermod -a -G gpio $USER

#insert into /etc/rc.local
chown -R root:gpio /sys/class/gpio
chmod -R ug+rw /sys/class/gpio

#add rule

sudo nano /etc/udev/rules.d/80-gpio-noroot.rules# /etc/udev/rules.d/80-gpio-noroot.rules

>>

# Corrects sys GPIO permissions on the Pine64 so non-root users in the gpio group can manipulate bits
#
# Change group to gpio
SUBSYSTEM=="gpio", PROGRAM="/bin/sh -c '/bin/chown -R root:gpio /sys/devices/soc.0/*pinctrl/gpio'"
# Change user permissions to ensure user and group have read/write permissions
SUBSYSTEM=="gpio", PROGRAM="/bin/sh -c '/bin/chmod -R ug+rw /sys/devices/soc.0/*pinctrl/gpio'"


#install docker

