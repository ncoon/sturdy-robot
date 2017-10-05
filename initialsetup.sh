#/bin/bash

# Creates the default directory to store termux scripts, then creates and edits a script which auto runs sturdy-robot on startup of termux.
# After that it creates an "update" script and alias to easily clone the repo to obtain the newest code.

mkdir /.termux/boot/
touch /.termux/boot/sturdyrobot.sh
chmod u+x /.termux/boot/sturdyrobot.sh
tee '#/bin/bash' >> /.termux/boot/sturdyrobot.sh
tee 'python2 ~/sturdy-robot/main.py' >> /.termux/boot/sturdyrobot.sh

touch update.sh
chmod u+x update.sh
tee '#/bin/bash' >> update.sh
tee 'rm -rf sturdy-robot' >> update.sh
tee 'git clone https://github.com/ncoon/sturdy-robot' >> update.sh
tee "alias update='./update.sh'" >> /etc/bash.bashrc
tee "alias sturdyrobot='python2 ~/sturdy-robot/main.py'" >> /etc/bash.bashrc
