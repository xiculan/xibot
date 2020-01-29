#!/bin/bash

#Install ffmpeg and other motion dependencies:
apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12

#Install motion:
wget https://github.com/Motion-Project/motion/releases/download/release-4.2.2/pi_buster_motion_4.2.2-1_armhf.deb
dpkg -i pi_buster_motion_4.2.2-1_armhf.deb

#note: Raspbian Buster comes with motion version 4.1; it is however recommended that you install version 4.2, as indicated above
#Install the dependencies from the repositories:
apt-get install python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev libz-dev

#Install motioneye, which will automatically pull Python dependencies (tornado, jinja2, pillow and pycurl):
pip install motioneye

#note: If pillow installation fails, you can try installing it from official repos using apt-get install python-pillow.
#Prepare the configuration directory:
mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

#Prepare the media directory:
#mkdir -p /var/lib/motioneye

#Add an init script, configure it to run at startup and start the motionEye server:
cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
systemctl daemon-reload
systemctl enable motioneye
systemctl start motioneye

#To upgrade to the newest version of motionEye, just issue:
pip install motioneye --upgrade
systemctl restart motioneye

#configurar motion******************
carpeta on es guarden les imatges


