#! /bin/sh

# editcap is part of the wireshark distribution and it does some
# nice things.

SIZE=1000
FILEIN=/export/external/SKAION2009/data/mypcap_20091103081848.pcap

FILEOUTDIR=/export/external/SKAION2009/data_$SIZE
FILEOUTNAME=mycap.pcap

mkdir -p $FILEOUTDIR
editcap -c $SIZE $FILEIN $FILEOUTDIR/$FILEOUTNAME 
