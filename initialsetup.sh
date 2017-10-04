#/bin/bash

# Creates the default directory to store termux scripts, then creates and edits a script which auto runs sturdy-robot on startup of termux.
# After that it creates an "update" script and alias to easily clone the repo to obtain the newest code.

mkdir ~/.termux/boot/
touch ~/.termux/boot/sturdyrobot.sh
chmod u+x ~/.termux/boot/sturdyrobot.sh
tee '#/bin/bash' >> ~/.termux/boot/sturdyrobot.sh
tee 'python2 ~/sturdy-robot/main.py' >> ~/.termux/boot/sturdyrobot.sh

touch ~/home/update.sh
chmod u+x ~/home/update.sh
tee '#/bin/bash' >> ~/home/update.sh
tee 'git clone https://github.com/ncoon/sturdy-robot' >> ~/home/update.sh
tee "alias update='./update.sh'" >> ~/.bashrc
tee "alias sturdyrobot='python2 ~/sturdy-robot/main.py'" >> ~/.bashrc
