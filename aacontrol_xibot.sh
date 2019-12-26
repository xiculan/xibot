#! /bin/bash
#xibot config
#name='xicu'
#static_ip='192.168.1.194'
#echo You are $name and the ip of this device is: $static_ip


#control -------------------------------------------------------------
backup='0'
update='0'
make_control_web='0'
install_control_pixhawk='1'

#backup most important files --------------------------------------------
if [ $backup = '1' ]
then
        sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.orig
fi

#update  --------------------------------------------------------
if [ $update = '1' ]
then
        sudo apt update >> /home/xicu/informe.txt
fi

#make control web  ---------------------------------------------------
if [ $make_control_web = '1' ]
then
        sudo cp ./xibot_web /var/www/html/
#	sudo ln -s /root/scripts scripts
          
        sudo rm /var/www/html/index.html
        sudo mv index.php /var/www/html/
fi

#make control web  ---------------------------------------------------
if [ $install_control_pixhawk = '1' ]
then
#	sudo apt-get install screen python-wxgtk2.8 python-matplotlib python-opencv python-pip python-numpy
    sudo apt-get install python-matplotlib python-opencv python-pip python-numpy
    sudo pip install mavproxy
fi


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
