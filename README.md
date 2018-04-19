sturdy-robot is a simple tool to help EMS practitioners. To run the code on an android device you can do the following steps:

PLEASE READ THE LICENSE DOCUMENT - GPLv3

#The following instructions can be copied from this site and pasted in "termux" by long pressing anywhere on the terminal.

	1 - Download "termux" and "termux:widget"(A free and open source app.) from the google play store(2.99$) or f-droid(FREE).

	2 - Open "termux" and run "apt update" and followed by "apt install git python2 nano" without quotations.

	3 - Again, with "termux" run "git clone https://github.com/ncoon/sturdy-robot" without quotations.

	Run the following commands:
	
	4 - Now you can run initial setup script! Simply change directories "cd sturdy-robot" (This will show no output)
	
	5 - "chmod u+x initialsetup.sh" (No output when run correctly) to give execute permissions to the setup script. 
	
	6 - "mv initialsetup.sh .." (No output when run correctly, make sure to run it with the ..)
	
	7 - "cd ..", and "./initialsetup.sh".
	
	8 - After the script has run, go to the your home screen and select to add a widget. Choose the "termux" widget to autolaunch sturdy-robot from your home screen.

	9 - In "termux" you can simply run "sturdyrobot" to execute the program, or "update" to download the newest version of "sturdy-robot". 
	
#Alternatively you may download the code and run it without termux by using another python interpreter. This code should be operating system agnostic.

#Feel free to copy the project and add your own scripts, please contact me if you do so as I'd like to add them to sturdy-robot!

#Step 2 explained: "apt update" tells "apt" (The Advanced Packaging Tool, a program which installs programs and their dependencies for you.) to update it's software lists or "repositories". Then "apt install git python2 nano" tells "apt" to install the software packages git (To download projects from github), python2 (the programming language required to run "sturdy-robot"), and nano (A simple text editor so that you can review the source code for "sturdy-robot").

#Step 3 explained: "git clone https://github.com/ncoon/sturdy-robot" tells the program "git" to download the contents of the url into a directory named "sturdy-robot". 

#Steps 4, 5, 6, 7 explained: "cd sturdy-robot" changes directories to the sturdy-robot directory. Using "chmod u+x" gives the current user execute permissions for the specified file. "cd .." moves up one directory (folder), and running "./" is a standard way to execute a script in a Linux environment.
 
#How to review the source code: "cd" into the sturdy-robot directory and then list all the files therein with the "ls" command.  Use the "nano" text editor to open any of the files for your review, for example "nano height.py". Press the hardware key "Volume Down" and the "x" on the keyboard at the same time to exit nano. You can also review the entire source code at this github page.

