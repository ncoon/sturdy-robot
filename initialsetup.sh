#!/bin/bash

# Creates four scripts and then aliases for easy calling of the scripts, run autolaunchsetup.sh to move a autolaunch script to ~/boot/

mkdir boot

touch ~/sturdyrobot.sh
chmod u+x ~/sturdyrobot.sh
echo '#!/bin/bash' > ~/sturdyrobot.sh
echo 'python2 ~/sturdy-robot/main.py' >> ~/sturdyrobot.sh # This runs the sturdy-robot program

touch ~/sturdyrobotauto.sh
chmod u+x ~/sturdyrobotauto.sh
echo '#!/bin/bash' > ~/sturdyrobotauto.sh
echo 'python2 ~/home/sturdy-robot/main.py' >> ~/sturdyrobotauto.sh #This script can be moved to ~/.termux/boot for auto launching of sturdyrobot

touch ~/autolaunchsetup.sh
chmod u+x ~/autolaunchsetup.sh
echo '#!/bin/bash' > ~/autolaunchsetup.sh
echo 'mv ~/sturdyrobotauto.sh ~/boot/sturdyrobotauto.sh'

touch ~/update.sh
chmod u+x ~/update.sh
echo '#!/bin/bash' >> ~/update.sh
echo 'rm -rf sturdy-robot' > ~/update.sh
echo 'git clone https://github.com/ncoon/sturdy-robot' >> ~/update.sh # This runs an update of the sturdy-robot code
echo "alias update='./update.sh'" > ../usr/etc/bash.bashrc
echo "alias sturdyrobot='python2 ~/sturdy-robot/main.py'" >> ../usr/etc/bash.bashrc # These lines create aliases for the scripts.
echo "alias sturdy-robot='python2 ~/sturdy-robot/main.py'" >> ../usr/etc/bash.bashrc
source ../usr/etc/bash.bashrc
