#! /bin/sh

COUNT=10000
# -s0 all data
# -n -t -q be quiet as possible
# -x spit out the hex of the packet
# -r file to read
tcpdump -s0 -n -t -q -x -r $1 -c $COUNT > $2
