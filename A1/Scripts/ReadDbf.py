import dbf
from dbfread import DBF
import os

dir  = "/home/ingared/Documents/NS_IP/UndergroundData"
streets = "LONDON_STREETS.dbf"
underground = "LONDON_UNDERGROUND.dbf"
count = 0
test1 = DBF(os.path.join(dir,streets))
for record in test1:
    if (count <= 100):
        print record
    count += 1

print '\n'
print " Total Edges in Streets  : " , count
print '\n'

count = 0
test2 = DBF(os.path.join(dir,underground))
for record in test2:
    if (count%100 == 0):
        print record
    count += 1

print '\n'
print " Total Edges in Underground Metro : " , count
print '\n'
