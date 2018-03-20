#! /bin/sh
############################
# Abaddon files
#FILE=/export/external/SKAION2009/data/mypcap_20091103081848.pcap
#FILE=/export/external/SKAION2009/data_1000/mycap_01162_20091103082005.pcap
#FILE=/export/external/SKAION2009/data_10000/mycap_00110_20091103082001.pcap
# local files.
FILE=/home/czhou2/Document/maccdc2012_00002.pcap

# The base of the filename for later use
BASE=`basename $FILE`
SIZE=5000
############################
# Database URIs for storing the data
#URI="mysql://packet:packetepsabre@localhost/packet"
#URI="mysql://packet:packetepsabre@abaddon/packet"
URI="sqlite:///notInGit/packet.db"
############################

############################
# Print out the date to keep track of how long the code takes to run
date
############################

############################
# Make some required directories
mkdir -p log/$BASE
mkdir -p notInGit
rm -rf log/$BASE/*
############################


############################
# Tips and hints for calling snort.
# -q quiet
# -r file to read
# -n number of packets to read
# -l directory for log
# -c configuration file to use
# -U UTC time
# -T test the configuration
############################
# The snort configuration files.
#SNORTCONF=../lib/snort.conf
#SNORTCONF=../lib/notInGit/etc/snort.conf
SNORTCONF=../lib/snort.conf
############################
# Run snort!
time snort -q -r $FILE -n $SIZE -l ./log/$BASE -c $SNORTCONF -U
############################

############################
# Put the data into a database
############################
# Clear the database
time python databaseSetup.py -d --URI=$URI
############################
# Make sure the database is set up
time python databaseSetup.py --URI=$URI
############################
# Upload the data into the database
time python toSQL.py -p --URI=$URI -f log/$BASE/unified2.log.*
############################
time python fromSQL.py

date
