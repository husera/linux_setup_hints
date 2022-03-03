# See also:
https://www.phoscon.de/en/raspbee2/install#raspbian

RTC-Installation
Install dependencies

 sudo apt update
 sudo apt install i2c-tools build-essential raspberrypi-kernel-headers
Download installation archive

 curl -O -L https://github.com/dresden-elektronik/raspbee2-rtc/archive/master.zip
 unzip master.zip
Change into extracted directory

 cd raspbee2-rtc-master
Compile RTC kernel module

 make
Install RTC kernel module

 sudo make install
Reboot Raspberry Pi

 sudo reboot
Configure system time to RTC module

 sudo hwclock --systohc
Test that RTC is working

 sudo hwclock --verbose
Waiting in loop for time from /dev/rtc0 to change
 ...got clock tick
 Time read from Hardware Clock: 2020/03/06 13:55:21
 Hw clock time : 2020/03/06 13:55:21 = 1583502921 seconds since 1969
 Time since last adjustment is 1583502921 seconds
 Calculated Hardware Clock drift is 0.000000 seconds
 2020-03-06 14:55:20.017097+01:00
 ######################################
