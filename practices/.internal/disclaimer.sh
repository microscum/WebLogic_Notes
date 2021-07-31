#!/bin/bash

hash='#'
sql='--'
java='//'
xml='<!--'
xmlend=' -->'

line=0
commentstart=''
commentmiddle=''
commentend=''

border1='------------------------------------------------------------------------'
border2='========================================================================'
bordermid1='--'
bordermid2='=='

#These are replaced with the correct characters for each file type
border=''
bordermid=''

function usage {
    echo -e "\nUsage: disclaimer.sh [path]\n"
}

#Set default folder
folder=/practices/tune

#Get argument count
argc=$#

if [ $argc -gt 1 ]; then
    #If more than 1 arg is passed, then something is wrong
    echo -e "\nToo many arguments passed!"
    usage
    exit 1
elif [ $argc == 1 ]; then
    #If 1 arg is set, then it should be a folder to search
    folder=$1
    if [ ! -d "$folder" ]; then
        echo -e "\nFolder does not exist!"
        usage
        exit 1
    fi
fi

echo -e "\nAdding ST-Curr standard disclaimer to files in $folder...\n"

cd $folder
#for file in `ls -1 **/*.py **/*.sh **/*.sql **/*.java **/*.xml **/*.txt **/*.html 2>/dev/null`
for file in `find . -regextype posix-egrep -regex ".*\.(py|sh|sql|java|xml|txt|html)$" -print`
do
    #echo $file
    ext=`echo $file | sed "s/^.*\.//"`
    #echo $ext
    if [ "$ext" == "py" -o "$ext" == "txt" ]; then
        line=1        
        commentstart=$hash
        commentmiddle=$hash
        commentend=''
        border=$border1
        bordermid=$bordermid1
    fi    
    if [ "$ext" == "sh" ]; then
        line=2
        commentstart=$hash
        commentmiddle=$hash
        commentend=''
        border=$border1
        bordermid=$bordermid1
    fi
    if [ "$ext" == "sql" ]; then
        line=1
        commentstart=''
        commentmiddle=''
        commentend=''
        border=$border1
        bordermid=$bordermid1
    fi
    if [ "$ext" == "java" ]; then
        line=1
        commentstart=$java
        commentmiddle=$java
        commentend=''
        border=$border1
        bordermid=$bordermid1
    fi
    if [ "$ext" == "html" -o "$ext" == "xml" ]; then
        line=2
        commentstart=$xml
        commentmiddle=' '
        commentend=$xmlend
        border=$border2
        bordermid=$bordermid2
    fi

    echo "File: $file Ext: $ext Comment: $commentstart $comentend"

disclaimer="\n\
$commentstart $border\n\
$commentmiddle $bordermid DISCLAIMER:\n\
$commentmiddle $bordermid    This script is provided for educational purposes only. It is NOT\n\
$commentmiddle $bordermid    supported by Oracle World Wide Technical Support.\n\
$commentmiddle $bordermid    The script has been tested and appears to work as intended.\n\
$commentmiddle $bordermid    You should always run new scripts on a test instance initially.\n\
$commentmiddle $bordermid\n\
$commentmiddle ${border}$commentend\n"

    #echo "DISCLAIMER="
    #echo -e $disclaimer

    #Insert line if it isn't already there
    if [ -z "`grep "DISCLAIMER:" $file`" ]; then
        echo -e "$file is missing disclaimer... inserting...\n"
        sed -i "${line}i\\${disclaimer}" $file
    else
        echo -e "Already has disclaimer, do nothing...\n"    
    fi
done
cd -
