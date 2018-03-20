import dpkt
import argparse
import datetime

parser = argparse.ArgumentParser(description='Disect packets.')
parser.add_argument('-f', '--filename',
                    help='PCAP filename.')
parser.add_argument('-c', '--count',type=int,
                    help='Number of packets to process.')
args = parser.parse_args()

f = open(args.filename,'r')
pcap = dpkt.pcap.Reader(f)

packetCount = 0
for ts, buf in pcap:
    print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(ts))
    eth = dpkt.ethernet.Ethernet(buf)
    print eth
    
    packetCount += 1
    if packetCount > args.count:
        break
