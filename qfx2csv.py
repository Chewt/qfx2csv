#!/usr/bin/python

from ofxtools.Parser import OFXTree
import sys

parser = OFXTree()
with open(sys.argv[1], 'rb') as fileobj:
    parser.parse(fileobj)
    ofx = parser.convert()


statements = ofx.statements
print(statements)

transactions = statements[0].transactions
print(transactions)
for trx in transactions:
    print(str(trx.dtposted).split(' ')[0] + ',', end='')
    print(str(trx.fitid) + ',', end='')
    print(str(trx.trnamt) + ',', end='')
    print(str(trx.name) + ',', end='')
    print(str(trx.memo) + ',', end='\n')
