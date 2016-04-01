import dbf
from dbfread import DBF
import os

dir  = "/home/ingared/Documents/NS_IP/UndergroundData"
streets = "LONDON_STREETS.dbf"
underground = "LONDON_UNDERGROUND.dbf"
ny_underground = "NY_UNDERGROUND.dbf"
ny_streets = "NY_STREETS.dbf"
count = 0
test1 = DBF(os.path.join(dir,ny_streets))
for record in test1:
    if (count <= 10):
        print record
    count += 1

print '\n'
print " Total Edges in Streets  : " , count
print '\n'

count = 0
b = {}

test2 = DBF(os.path.join(dir,ny_underground))
for record in test2:
    if (count%100 == 0):
        print record
    count += 1

print '\n'
print " Total Edges in Underground Metro : " , count
print '\n'

