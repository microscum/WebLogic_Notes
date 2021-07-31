#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------


#This script makes it convenient for students to switch session persistence types for the ShoppingCart application

#Command line:
# Default: memory
# -memory: replicated
# -file: file
# -jdbc: jdbc

bindir=/practices/tune/bin
source $bindir/checkoracle.sh
source $bindir/checkhost01.sh

reptype="memory"
practicedir=$PWD

#Clean up any previously persisted data
echo "Cleaning up any previous file or JDBC persisted sessions..."
rm -rf sessions
ssh host02 "cd $practicedir; ./deleteSessionDB.sh" 2>/dev/null >&2

#Check to see if an argument was passed. We will only deal with arg1
if [ ! -z "$1" ]; then
	if [ "$1" == "-memory" ]; then
		reptype="memory"
        #No extra configuration needed
	fi	
	if [ "$1" == "-file" ]; then
		reptype="file"
        #Create the file store directory
        echo "Creating File store directory for sessions: ./sessions"
		mkdir sessions
	fi
	if [ "$1" == "-jdbc" ]; then
		reptype="jdbc"
        #Create the HTTP sessions database table
        echo "Creating wl_servlets_sessions on database on host02"
		ssh host02 "cd $practicedir; ./createSessionDB.sh"
	fi
fi

#Inform the student which session persistence type that you think is set
echo -e "\n***********************"
echo "SESSION TYPE=${reptype}"
echo "***********************"

#Set the correct configuration weblogic.xml file to use
config="resources/${reptype}/weblogic.xml"

#Copy the correct configuration to the ShoppingCart application
cp $config resources/ShoppingCart/WEB-INF

#Only redeploy if not part of resetting the env
if [ "$2" != "-reset" ]; then
    #Redeploy the ShoppingCart application with the new session persistence configuration
    ./redeploy.sh
fi

echo -e "\nSet $config for ShoppingCart application..\n"


