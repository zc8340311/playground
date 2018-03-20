#! /usr/bin/env python

import sqlalchemy as sql
import argparse

metadata = sql.MetaData()
packets = sql.Table('packets', metadata,
                    sql.Column('id', sql.Integer, primary_key=True),
                    sql.Column('time', sql.DateTime),
                    sql.Column('sourceIP1',sql.SmallInteger),
                    sql.Column('sourceIP2',sql.SmallInteger),
                    sql.Column('sourceIP3',sql.SmallInteger),
                    sql.Column('sourceIP4',sql.SmallInteger),
                    sql.Column('sourcePort',sql.Integer),
                    sql.Column('destinationIP1',sql.SmallInteger),
                    sql.Column('destinationIP2',sql.SmallInteger),
                    sql.Column('destinationIP3',sql.SmallInteger),
                    sql.Column('destinationIP4',sql.SmallInteger),
                    sql.Column('destinationPort',sql.Integer),
                    sql.Column('signatureID',sql.Integer),
                    sql.Column('packet',sql.LargeBinary),
)

def dropTable(args):
    engine = sql.create_engine(args.URI)
    packets.drop(engine)

def createTable(args):
    engine = sql.create_engine(args.URI)
    metadata.create_all(engine) 

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Creat or drop the table in the database.')
    parser.add_argument('-d', '--drop', action='store_true',
                        help='Drop the table rather than creating it.')
    parser.add_argument('--URI',
                        help='The database URI.')

    args = parser.parse_args()

    if args.drop:
        dropTable(args)
    else:
        createTable(args)
