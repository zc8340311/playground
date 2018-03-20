import sqlalchemy as sql
import numpy as np
import databaseSetup
import struct
#import matplotlib.pylab as py

URI="sqlite:///notInGit/packet.db"
engine = sql.create_engine(URI)
conn = engine.connect()
packets = databaseSetup.packets

s = sql.select([packets.c.sourceIP1,
                packets.c.sourceIP2,
                packets.c.sourceIP3,
                packets.c.sourceIP4,
                packets.c.sourcePort,
                packets.c.destinationIP1,
                packets.c.destinationIP2,
                packets.c.destinationIP3,
                packets.c.destinationIP4,
                packets.c.destinationPort,
                packets.c.packet])
result = conn.execute(s)
result = list(result)
numpackets =  len(result)
maxlen = 1520 # This is a MTU I think.
data = np.empty([numpackets,maxlen],dtype=np.uint8)

y =  np.empty([numpackets,10],dtype=np.uint8)

print 'numpackets: ',numpackets
i = 0
# print 'sourceIP1, sourceIP2, sourceIP3, sourceIP4, sourcePort,',
# print 'destinationIP1, destinationIP2, destinationIP13, destinationIP4, destinationPort'
for row in result:
    # print '%d, %d, %d, %d, %d,'%(row[0],row[1],row[2],row[3],row[4]),
    # print '%d, %d, %d, %d, %d'%(row[5],row[6],row[7],row[8],row[9])
    y[i] = row[:10]
    for j in xrange(len(row[10])):
        data[i,j] = struct.unpack('B',row[10][j])[0]
    i += 1

np.save('notInGit/packets.npy',data)
np.save('notInGit/y.npy',y)
#py.imshow(data)
#py.show()
