echo 'console=display' >> /boot/armbianEnv.txt
systemctl mask serial-getty@ttyS2.service || true
systemctl mask serial-getty@ttyFIQ0       || true
