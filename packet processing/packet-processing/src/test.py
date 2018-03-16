from idstools import unified2
import glob

filename=glob.glob('log/unified2.log.*')[0]
reader = unified2.FileRecordReader(filename)
totalRecords = 0
totalEvents = 0
totalPackets = 0
totalUDPprot = 0
totalTCPprot = 0
totalICMPprot = 0
totalUDP = 0
totalTCP = 0
totalICMP = 0

for record in reader:
    if type(record) == unified2.Event:
        totalEvents += 1
        if record['protocol'] == 1:
            totalICMPprot += 1
        elif record['protocol'] == 6:
            totalTCPprot += 1
        elif record['protocol'] == 17:
            totalUDPprot += 1

        if record['signature-id'] == 1000001:
            totalTCP += 1
        elif record['signature-id'] == 1000002:
            totalUDP += 1
        elif record['signature-id'] == 1000003:
            totalICMP += 1
        
    if type(record) == unified2.Packet:
        totalPackets += 1
    totalRecords += 1
print 'totalPackets',totalPackets
print 'totalEvents',totalEvents
print 'totalRecords',totalRecords

print 'totalICMPprot',totalICMPprot
print 'totalTCPprot',totalTCPprot
print 'totalUDPprot',totalUDPprot

print 'totalICMP',totalICMP
print 'totalTCP',totalTCP
print 'totalUDP',totalUDP

