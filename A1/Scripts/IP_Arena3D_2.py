import dbf
from dbfread import DBF
import os

dir  = "D:\Downloads\Strano_et_al_multiplex_city_data"
streets = "LONDON_STREETS.dbf"
underground = "LONDON_UNDERGROUND.dbf"
ny_underground = "NY_UNDERGROUND.dbf"
ny_streets = "NY_STREETS.dbf"
count = 0
test1 = DBF(os.path.join(dir,ny_streets))
NY_street = []
NY_underground = []

IP_Street_Connections = open('D:\Downloads\Arena3D_v2.0\Arena3D_v2.0\Input Files Examples\IP_StrUnd_Connections.txt','w',encoding='utf-8')
IP_Street_Connections.write("start_connections" + "\n")

for record in test1:
	fn_id = record['FN_ID']
	tn_id = record['TN_ID']
	length = record['length']
	if fn_id not in NY_street:
		NY_street.append(fn_id)
	if tn_id not in NY_street:
		NY_street.append(tn_id)
	IP_Street_Connections.write(str(fn_id) + "::nystreets" + "	" + str(tn_id) + "::nystreets" + "	" + str(length))
	IP_Street_Connections.write("\n")

test2 = DBF(os.path.join(dir,ny_underground))
for record in test2:
	fn_id = record['FN_ID']
	tn_id = record['TN_ID']
	length = record['length']
	if fn_id not in NY_underground:
		NY_underground.append(fn_id)
	if tn_id not in NY_underground:
		NY_underground.append(tn_id)
	IP_Street_Connections.write(str(fn_id) + "::nyunderground" + "	" + str(tn_id) + "::nyunderground" + "	" + str(length))
	IP_Street_Connections.write("\n")

for i,j in zip(NY_street,NY_underground):
	if(i==j):
		IP_Street_Connections.write(str(i) + "::nystreets" + "	" + str(i) + "::nyunderground")
		IP_Street_Connections.write("\n")

IP_Street_Connections.write("end_connections")

print("Number of street junctions:" , len(NY_street))
print("Number of underground stations:" , len(NY_underground))
IP_Street_Connections.close()


