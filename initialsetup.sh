#/bin/bash

# Creates the default directory to store termux scripts, then creates and edits a script which auto runs sturdy-robot on startup of termux.
# After that it creates an "update" script and alias to easily clone the repo to obtain the newest code.

mkdir ~/termux/boot/
touch ~/com.termux/boot/sturdyrobot.sh
chmod u+x ~/com.termux/boot/sturdyrobot.sh
echo '#/bin/bash' >> ~/com.termux/boot/sturdyrobot.sh
echo 'python2 ~/sturdy-robot/main.py' >> ~/com.termux/boot/sturdyrobot.sh

touch ~/update.sh
chmod u+x ~/update.sh
echo '#/bin/bash' >> ~/update.sh
echo 'rm -rf sturdy-robot' >> ~/update.sh
echo 'git clone https://github.com/ncoon/sturdy-robot' >> ~/update.sh
echo "alias update='./update.sh'" >> /usr/etc/bash.bashrc
echo "alias sturdyrobot='python2 ~/sturdy-robot/main.py'" >> /usr/etc/bash.bashrc
