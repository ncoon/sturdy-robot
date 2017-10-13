#/bin/bash

# Creates two scripts and then aliases for easy calling of the scripts



touch ~/sturdyrobot.sh
chmod u+x ~/sturdyrobot.sh
echo '#/bin/bash' > ~/sturdyrobot.sh
echo 'python2 ~/sturdy-robot/main.py' >> ~/sturdyrobot.sh # This runs the sturdy-robot program

touch ~/update.sh
chmod u+x ~/update.sh
echo '#/bin/bash' >> ~/update.sh
echo 'rm -rf sturdy-robot' > ~/update.sh
echo 'git clone https://github.com/ncoon/sturdy-robot' >> ~/update.sh # This runs an update of the sturdy-robot code
echo "alias update='./update.sh'" > ../usr/etc/bash.bashrc
echo "alias sturdyrobot='python2 ~/sturdy-robot/main.py'" >> ../usr/etc/bash.bashrc # These lines create aliases for the scripts.
echo "alias sturdy-robot='python2 ~/sturdy-robot/main.py'" >> ../usr/etc/bash.bashrc
source ../usr/etc/bash.bashrc
