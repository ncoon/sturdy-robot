<<sturdy-robot>> is a simple tool to help EMS practitioners. To run the code on an android device you can do the following steps:

PLEASE READ THE LICENSE DOCUMENT - GPLv3

	1 - Download "termux"(A free and open source app.) from the google play store or f-droid.

	2 - Open "termux" and run "apt update" and followed by "apt install git python2 nano" without quotations.

	3 - Again, with "termux" run "git clone https://github.com/ncoon/sturdy-robot" without quotations.

	4 - Now you can run the code! Simply change directories "cd sturdy-robot" followed by "python2 main.py".
	
	*Updating the program. As of yet there is no automatic update function, so you'll have to open "termux" and run STEP 3 again. 

#Alternatively you may download the code and run it without termux by using another python interpreter. This code should be operating system agnostic.

#Feel free to copy the project and add your own scripts, please contact me if you do so as I'd like to add them to sturdy-robot!

#Step 2 explained: "apt update" tells "apt" (The Advanced Packaging Tool, a program which installs programs and their dependencies for you.) to update it's software lists or "repositories". Then "apt install git python2 nano" tells apt to install the software packages git (To download projects from github), python2 (the programming language required to run "sturdy-robot") and nano (A simple text editor so that you can review the source code for "sturdy-robot").

#Step 3 explained: "git clone https://github.com/ncoon/sturdy-robot" tells the program "git" to download the contents of the url into a directory named "sturdy-robot". 

#Step 4 explained: "cd sturdy-robot" changes directories to the sturdy-robot directory. You can then execute the program by running "python2 main.py" which tells termux to run main.py as a python program.
 
#How to review the source code: "cd" into the sturdy-robot directory and then list all the files therein with the "ls" command.  Use the "nano" text editor to open any of the files for your review, for example "nano height.py". Press the hardware key "Volume Down" and the "x" on the keyboard at the same time to exit nano.

