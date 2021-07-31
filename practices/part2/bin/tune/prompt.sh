#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#######################################################################################################
## Oracle Server Technologies Lab Framework
## File:     prompt.sh
## Author:   TJ Palazzolo
## Modified: Feb 9, 2013 Mark Lindros
## Modified: Jul 30, 2013 Mark Lindros: Removed call to setWLSEnv.sh because the main setenv calls it now
## Description:
## This script launches a new Unix shell process.
## Several system variables are set for the student's convenience and to aid in the use of the Lab Framework.
## The script setWLSEnv is executed to initialize standard WebLogic variables such as JAVA_HOME and CLASSPATH.
## Developers are expected to update this script as necessary to match their local WebLogic environment.
#######################################################################################################

gnome-terminal --title "LABS: prompt.sh" --geometry=90x30 &
exit
