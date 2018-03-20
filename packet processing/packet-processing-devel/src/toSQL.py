#! /usr/bin/env python

from idstools import unified2
import argparse
import sqlalchemy as sql
import datetime
import databaseSetup

def run(args):
    engine = sql.create_engine(args.URI)
    conn = engine.connect()

    totalRecords = 0
    totalEvents = 0
    totalPackets = 0
    totalUDPprot = 0
    totalTCPprot = 0
    totalICMPprot = 0
    totalUDP = 0
    totalTCP = 0
    totalICMP = 0
    totalOther = 0

    # The number of packets to collect before sending to the database.
    # This is an optimization!
    maxPackets = 10000
    packetList = []

    for filename in args.filename:
        if (not args.count is None) and totalEvents > args.count:
            break

        reader = unified2.FileRecordReader(filename)
        fileRecords = 0
        for record in reader:
            totalRecords += 1
            fileRecords += 1
            totalEvents += 1

            if (not args.count is None) and totalEvents > args.count:
                break

            # Note, this is a tricky little conditional.  We don't know it is
            # an EVent until after the test of the type.  So, it
            # will fail before it trys to access the 'source-ip.raw'
            # key (which would be an exception if it got that far and
            # the recors wasn't an event).
            # We look at the length of 'source-ip.raw' to see if it
            # is a IPv4 packet or not.  We are not setup (yet!) to process
            # IPv6 packets.
            if type(record) == unified2.Event and len(record['source-ip.raw']) == 4:
                ts = record['event-second']+\
                     record['event-microsecond']/1000000.
                packetTime = datetime.datetime.utcfromtimestamp(ts)
                sourceIP = map(int,record['source-ip'].split('.'))
                destIP = map(int,record['destination-ip'].split('.'))

                # After the event is the packet that set it off.
                packet = reader.next()
                totalRecords += 1

                if type(packet) == unified2.Packet:
                    totalPackets += 1
                    data = packet['data']
                else:
                    data =[]

                packetList.append({'time': packetTime, 
                     'sourceIP1':sourceIP[0],
                     'sourceIP2':sourceIP[1],
                     'sourceIP3':sourceIP[2],
                     'sourceIP4':sourceIP[3],
                     'sourcePort':record['sport-itype'],
                     'destinationIP1':destIP[0],
                     'destinationIP2':destIP[1],
                     'destinationIP3':destIP[2],
                     'destinationIP4':destIP[3],
                     'destinationPort':record['dport-icode'],
                     'signatureID':record['signature-id'],
                     'packet':data
                 })

                # We only submit packets every once in a while to make
                # the code more efficient.
                if len(packetList) > maxPackets:
                    print 'inserting %d packets into database'%len(packetList)
                    conn.execute(databaseSetup.packets.insert(), packetList)
                    packetList = []

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
                else:
                    print record
                    totalOther +=1
    # Submit the last few packets in this file.
    if len(packetList) > 0:
        print 'inserting %d packets into database'%len(packetList)
        conn.execute(databaseSetup.packets.insert(), packetList)
        packetList = []

        print 'filename', filename
    print 'fileRecords', fileRecords

    conn.close()

    print 'totalEvents', totalEvents
    print 'totalRecords', totalRecords
    print 'totalPackets', totalPackets
    print 'totalOther',totalOther

    print 'totalICMPprot', totalICMPprot
    print 'totalTCPprot', totalTCPprot
    print 'totalUDPprot', totalUDPprot

    print 'totalICMP', totalICMP
    print 'totalTCP', totalTCP
    print 'totalUDP', totalUDP

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Read unified2.')
    parser.add_argument('-f', '--filename', nargs='*',
                        help='PCAP filename.')
    parser.add_argument('-c', '--count', type=int, default=None,
                        help='Number of packets to process.')
    parser.add_argument('-p', '--profile', action='store_true',
                        help='Turn on profiling.')
    parser.add_argument('--URI',
                        help='The database URI.')
    args = parser.parse_args()
    
    if args.profile:
        import cProfile,pstats
        cProfile.run('run(args)','notInGit/toSQL.stats')
        p = pstats.Stats('notInGit/toSQL.stats')
        p.strip_dirs().sort_stats('cumtime').print_stats()
    else:
        run(args)
