#!/bin/bash

#----------------------------------------------------
[ -z $BASH ] || shopt -s expand_aliases
alias BEGINCOMMENT="if [ ]; then"
alias ENDCOMMENT="fi"
#--------------------------------------------------------
# Allows us to read user input below, assigns stdin to keyboard
exec < /dev/tty
echo "Enter Option and Press [ENTER] or just [ENTER] to run the program"
echo "0. Set up IP addresses"
echo "1. Print help"
read answer 
# echo "ans is " $answer
if [ "$answer" == "0" ]; then
	exit ERRCODE "Check the ip addresses using ifconfig"
fi

if [ "$answer" == "1" ]; then
	echo ""
	echo "This is simple Data Transfer Application. Read Instructions"
	echo "1. All the routers should be configured manually to update FIB for particular prefix names"
	echo "2. 'Dropbox/Thesis/files/' folder should contain the files to be hosted"
fi

#BEGINCOMMENT
#-----------------------------------------------------------
sourceIp="udp://192.168.56.105"	#not needed
routerIp="udp://192.168.56.106"
destinationIp="udp://192.168.56.107"

if [ $1 -eq 1 ]; then
	echo "Setting up Consumer - Host 1"
	# system #1 - consumer
	# manually add path to divert traffic to the intermediate router
	# all the requests starting with /files will be sent to router.
	# face should point to ip address of router
	nfdc face create $routerIp
	nfdc route add ndn:/files/ $routerIp
	nfdc route add ndn:/good/ $routerIp
	echo "Ready Host 1..."
fi


if [ $1 -eq 2 ]; then
	echo "Setting up Router - Host 2"
	# system #2 - router
	# manually add path to divert traffic to end destination
	# all incoming requests starting with /files will be sent producer.
	# face should point to ip address of router
	nfdc face create $destinationIp
	nfdc route add ndn:/files/ $destinationIp
	nfdc route add ndn:/good/ $destinationIp
	echo "Ready Host 2..."
fi


if [ $1 -eq 3 ]; then
	echo "Setting up Producer - Host 3"
	# system #3 - producer
	# configure producer here. Mention all the files hosted by the producer. 
	# Mention the  expected interest names as well.
	# producer sends reply	
	# -v is removed. & runs the process in background
	unrar e files.rar files/ 
	
	ndnpingserver ndn:/good/morning &	# should be first command
	ndnputchunks  ndn:/files/hello.txt < files/hello.txt &
	ndnputchunks  ndn:/files/1KB.txt < files/1KB.txt &
	ndnputchunks  ndn:/files/10MB.txt < files/10MB.txt &
	ndnputchunks  ndn:/files/100MB.txt < files/100MB.txt &
	
	echo "Ready Host 3..."
fi

# 31 request 1st published file. 32 requests second published file and so on.
if [ $1 -eq 31 ]; then
	ndncatchunks -d iterative -v ndn:/files/hello.txt
fi

if [ $1 -eq 32 ]; then
	ndncatchunks -d iterative -v ndn:/files/1KB.txt
fi

if [ $1 -eq 33 ]; then
	ndncatchunks -d iterative -v ndn:/files/10MB.txt
fi

if [ $1 -eq 34 ]; then
	ndncatchunks -d iterative -v ndn:/files/100MB.txt
fi


BEGINCOMMENT
pending 

// connect to testbed - see the throughput
// use nfd disect tools to send interest

https://yoursunny.com/t/2016/ndncert/


modify the dissect tool
this gives what i want
ndnpeek ndn:/localhost/nfd/status/general | ndn-dissect

see the cpu usage

sending interest
ndn-cxx/example/consumer.cpp


ndnpingserver ndn:/morning &
ndnping ndn:/morning -c1


ENDCOMMENT
