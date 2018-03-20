#! /bin/sh
SIZE=10000
FILE=../dataSmall/foo_00000_20091103081848.pcap
date
mkdir -p log
rm -f log/*
# -q quite
# -r file to read
# -n number of packets to read
# -l directory for log
# -c configuration file to use
# -U UTC time
snort -q -r $FILE -n $SIZE -l ./log -c snort.conf -U

#https://www.wireshark.org/docs/dfref/
# -t ud : UTC time with date
# -c : count of packets
# -r : file to read
# -T fields : print out fields (i.e., CSV)
# -e : the columns to have
# -E : format options for the fields
# -Y : filter the packets, in this case just have ICMP, TCP, and UDP
tshark -n -t ud -c $SIZE -r $FILE -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e data -E header=y -E separator=, -E quote=d -E occurrence=f -Y "ip.proto==1 or ip.proto==6 or ip.proto==17" > log/tshark.csv

wc -l log/tshark.csv
python test.py

date
