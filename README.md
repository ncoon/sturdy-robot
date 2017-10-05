<<sturdy-robot>> is a simple tool to help EMS practitioners. To run the code on an android device you can do the following steps:

PLEASE READ THE LICENSE DOCUMENT - GPLv3

	1 - Download "termux"(A free and open source app.) from the google play store or f-droid.

	2 - Open "termux" and run "apt update" and followed by "apt install git python2 nano proot" without quotations.

	3 - Again, with "termux" run "git clone https://github.com/ncoon/sturdy-robot" without quotations.

	4 - Now you can run initial setup script! Simply change directories "cd sturdy-robot", followed by "chmod u+x   	    initialsetup.sh" to give execute permissions to the setup script. Then run "./initialsetup.sh".
	
	5 - After the script has run, you can simply run "sturdyrobot" to execute the program inside "termux", or "update" to 		  download the newest version of "sturdy-robot". 
#Alternatively you may download the code and run it without termux by using another python interpreter. This code should be operating system agnostic.

#Feel free to copy the project and add your own scripts, please contact me if you do so as I'd like to add them to sturdy-robot!

#Step 2 explained: "apt update" tells "apt" (The Advanced Packaging Tool, a program which installs programs and their dependencies for you.) to update it's software lists or "repositories". Then "apt install git python2 nano proot" tells "apt" to install the software packages git (To download projects from github), python2 (the programming language required to run "sturdy-robot"), nano (A simple text editor so that you can review the source code for "sturdy-robot"), and proot (Required to be able to modify files like bash.bashrc).

#Step 3 explained: "git clone https://github.com/ncoon/sturdy-robot" tells the program "git" to download the contents of the url into a directory named "sturdy-robot". 

#Step 4 explained: "cd sturdy-robot" changes directories to the sturdy-robot directory. Using "chmod u+x" gives the current user execute permissions for the specified file. Running "./" is a standard way to execute a script in a Linux environment.
 
#How to review the source code: "cd" into the sturdy-robot directory and then list all the files therein with the "ls" command.  Use the "nano" text editor to open any of the files for your review, for example "nano height.py". Press the hardware key "Volume Down" and the "x" on the keyboard at the same time to exit nano. You can also review the entire source code at this github page.

