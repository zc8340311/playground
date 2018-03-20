#! /bin/sh

#https://www.wireshark.org/docs/dfref/
# -O : only do the given protocol
# -t ud : UTC time with date
# -c : count of packets
# -r : file to read
# -T fields : print out fields (i.e., CSV)
# -e : the columns to have
# -E : format options for the fields
# -Y : filter the packets, in this case just have ICMP, TCP, and UDP
#tshark -O TCP -t ud -c $SIZE -r $FILE -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e data -E header=y -E separator=, -E quote=d -E occurrence=f -Y "ip.proto==1 or ip.proto==6 or ip.proto==17" > log/tshark.csv

time tshark -O TCP -t ud -c $SIZE -r $FILE -T fields -e frame.time -e ip.dst -e ip.src -e tcp.srcport -e tcp.dstport -e tcp.segment_data -e tcp.flag.ack -e tcp.len -E header=y -E separator=, -E quote=d -E occurrence=f > log/$BASE/tshark.csv
