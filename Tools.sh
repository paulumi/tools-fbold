n#!/bin/bash
#version 1.0

clear
# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

cowsay -f eyes "ND" | lolcat
figlet -f slant "ND" | lolcat
echo "    <////////////////////////[]\\\\\\\\\\\\\\\\\\>" | lolcat
echo "    <+++++++[       Tools By ND       ]+++++++>" | lolcat
echo  "    <~~~~~~~[  WA ND : 0819XXXXXXX34  ]~~~~~~~>" | lolcat
echo "    <=====================[]====================>" | lolcat

sleep 1

###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
clear
sleep 1
exit
}


lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo $b "1. Hack Akun Ig${enda}";
echo $b "2. Hack Akun FbOld${enda}";
echo $b "3. Multi BruteForce FbOld${enda}";
echo $b "4. Websc${enda}";
echo $b "5. Spam Jd.id${enda}";
echo $b "6. Tools ND${enda}";
echo $b "7. Spam Telkomsel${enda}";
echo $b "8. Install Bahan Cuk${enda}";
echo $b "99. Exit${enda}";
read -p " Pilih Nomornya =>" pil;

case $pil in
1) sh Ig.sh
echo

;;
2) python2 Fb.py

;;
3) python2 nd.py

;;
4) sh bh.sh

;;
5) php fs.php

;;

6) sh fs.sh

;;

7) php xc.php

;;

8) sh xd.sh

;;

99) echo "Autor : ND" | lolcat
figlet -f slant "ND" | lolcat
exit
;;

esac
done
done
