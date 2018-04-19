sturdy-robot is a simple tool to help EMS practitioners. To run the code on an android device you can do the following steps:

PLEASE READ THE LICENSE DOCUMENT - GPLv3

Before beginning go to https://f-droid.org (or Google Play) and install the "termux" and "termux:widget" apps. 

Termux copy and paste instructions

1 - apt update && apt install git python2 nano

2 - git clone https://github.com/ncoon/sturdy-robot

3 - cd sturdy-robot

4 - chmod u+x initialsetup.sh

5 - mv initialsetup.sh .. (Be sure to include the ..)

6 - cd ..

7 - ./initialsetup.sh

8* - update (To get new versions of sturdy-robot later on.)

Verbose instructions

1 - Open "termux" and run "apt update" and followed by "apt install git python2 nano" without quotations.

2 - Again, with "termux" run "git clone https://github.com/ncoon/sturdy-robot" without quotations.

Run the following commands:
	
3 - Simply change directories "cd sturdy-robot" (This will show no output)
	
4 - "chmod u+x initialsetup.sh" (No output when run correctly) to give execute permissions to the setup script. 
	
5 - "mv initialsetup.sh .." (No output when run correctly, make sure to run it with the ..)
	
6 - "cd ..", and "./initialsetup.sh". (No output)
	
7 - After the script has run, go to the your home screen and select to add a widget. Choose the "termux" widget to autolaunch sturdy-robot from your home screen.

8 - In "termux"(Open the app, not the widget) you can simply run "update" to download the newest version of "sturdy-robot". 


	
#Alternatively you may download the code and run it without termux by using another python interpreter. This code should be operating system agnostic.

#Feel free to copy the project and add your own scripts, please contact me if you do so as I'd like to add them to sturdy-robot!

#Step 2 explained: "apt update" tells "apt" (The Advanced Packaging Tool, a program which installs programs and their dependencies for you.) to update it's software lists or "repositories". Then "apt install git python2 nano" tells "apt" to install the software packages git (To download projects from github), python2 (the programming language required to run "sturdy-robot"), and nano (A simple text editor so that you can review the source code for "sturdy-robot").

#Step 3 explained: "git clone https://github.com/ncoon/sturdy-robot" tells the program "git" to download the contents of the url into a directory named "sturdy-robot". 

#Steps 4, 5, 6, 7 explained: "cd sturdy-robot" changes directories to the sturdy-robot directory. Using "chmod u+x" gives the current user execute permissions for the specified file. "cd .." moves up one directory (folder), and running "./" is a standard way to execute a script in a Linux environment.
 
#How to review the source code: Either read the code at https://github.com/ncoon/sturdy-robot or (using "termux")"cd" into the sturdy-robot directory and then list all the files therein with the "ls" command. Use the "nano" text editor to open any of the files for your review, for example "nano height.py". Press the hardware key "Volume Down" and the "x" on the keyboard at the same time to exit nano.

