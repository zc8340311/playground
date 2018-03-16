#! /bin/sh

# rawshark is a version of wireshark that seems to not process
# the packets as much as tshark.

# The -d option is important, this tells it how to process the packets.
tcpdump -r foo_00000_20091103081848.pcap -w - | rawshark -d encap:EN10MB -l -r- -s -F ip.dst -F tcp.segment_data
