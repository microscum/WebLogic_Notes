#!/bin/bash

# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. It is NOT
# --    supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# --
# ------------------------------------------------------------------------

#This script sets new custom variables for starting domains


#AdminServer uses default settings, while managed servers use custom settings
if [ "${SERVER_NAME}" != "AdminServer" ]; then

    ##############################################################################
    # Comment out what is not needed and uncomment settings for the current step #
    ##############################################################################

    #export USER_MEM_ARGS="-Xms50m -Xmx50m -XX:MaxPermSize=256m"
    #export USER_MEM_ARGS="-Xms90m -Xmx90m -XX:MaxPermSize=256m"

#Set GC logging
    #JAVA_OPTIONS+=" -XX:+PrintCommandLineFlags"
    #JAVA_OPTIONS+=" -XX:+PrintGC"
    #JAVA_OPTIONS+=" -XX:+PrintGCDetails"
    #JAVA_OPTIONS+=" -XX:+PrintGCTimeStamps"
    #JAVA_OPTIONS+=" -Xloggc:/tmp/gc.log"
    #JAVA_OPTIONS+=" -verbose:gc"

#Set GC type
    #JAVA_OPTIONS+=" -XX:+UseSerialGC"
    #JAVA_OPTIONS+=" -XX:+UseParallelGC"
    #JAVA_OPTIONS+=" -XX:+UseParallelOldGC"
    #JAVA_OPTIONS+=" -XX:+UseParNewGC"
    #JAVA_OPTIONS+=" -XX:+UseConcMarkSweepGC"
    #JAVA_OPTIONS+=" -XX:+UseG1GC"

    #JAVA_OPTIONS+=" -XX:+UnlockCommercialFeatures"
    #JAVA_OPTIONS+=" -XX:+FlightRecorder"

    #export JAVA_OPTIONS
fi


