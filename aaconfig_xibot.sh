#! /bin/bash
#xibot config
#name='xicu'
#static_ip='192.168.1.194'
#echo You are $name and the ip of this device is: $static_ip


#date
backup='0'
update='0'
basic_configurations='0'
make_links='0'
install_apache='0'
install_basic_xibot_software='0'
change_to_static_ip='0'
install_motion='1'

#backup most important files --------------------------------------------
if [ $backup = '1' ]
then
        sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.orig
fi

#make links --------------------------------------------------------------
if [ $make_links = '1' ]
then
    sudo ln -s /var/www/html /root/htm
    sudo ln -s /var/www/html /home/xicu/htm
    sudo ln -s /home/xicu /root/xicu
    sudo ln -s /media/ele /home/xicu/ele
    sudo ln -s /media/ele/cose /home/xicu/cose

fi

#update raspberry --------------------------------------------------------
if [ $update = '1' ]
then
        sudo apt update >> /home/xicu/informe.txt
fi

# basic configurations ---------------------------------------------------
if [ $basic_configurations = '1' ]
then
        sudo mkdir /home/xicu/scripts
        sudo mkdir /tmp/trash
	sudo ln -s /root/scripts scripts
fi

#change to static ip ------------------------------------------------------
if [ $change_to_static_ip = '1' ]
then
        echo '#interface eth0' >> /etc/dhcpcd.conf
        #static ip_address=192.168.0.10/24
        #static ip6_address=fd51:42f8:caae:d92e::ff/64
        #static routers=192.168.0.1
        #static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
fi

#install basic software ------------------------------------------------------
if [ $install_basic_xibot_software = '1' ]
then
#	sudo apt install samba
	echo 'hola'

fi

#install motion ----------------------------------------------------------------
if [ $install_motion = '1' ]
then
#	sudo apt install autoconf automake build-essential pkgconf libtool git libzip-dev libjpeg-dev gettext libmicrohttpd-dev libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev default-libmysqlclient-dev libpq-dev libsqlite3-dev libwebp-dev
#	cd /tmp
#	sudo wget https://github.com/Motion-Project/motion/releases/download/release-4.2.2/pi_buster_motion_4.2.2-1_armhf.deb
#	sudo dpkg -i pi_buster_motion_4.2.2-1_armhf.deb
	apt install motion


fi



#zona funcions ********************************************************************
#**********************************************************************************
sayhello()
{
   echo 'hello:la funcion se ha ejecutado'
}

#function
check_installed_soft()
{

}

#linea:136

# backup on hot
#


# *******************************************************************************
#configurar raspbian buster *************************
# entrar como usuario pi
# pasar a root i cambiar contraseña
# crear usuario xicu

# eliminar usuario pi

# entrar como usuario pi ssh


# cambiar puerto ssh


#software **********************************
# open vpn
# rpi monitor
# python
# java
# glances
# apache

#links:***************************
#https://rpi-experiences.blogspot.com/p/rpi-monitor-installation.html



#codi exemple *************************************************

#myfunc() {
#    echo "Using functions"
#}
#total=1
#while [ $total -le 3 ]; do
#    myfunc
#    total=$(($total + 1))
#done
#echo "Loop finished"
#myfunc
#echo "End of the script"
