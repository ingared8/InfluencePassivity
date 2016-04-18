import numpy as np

def generate_graph_data(layers,nodes):

	#Intra_layer connnections
	all_layers_filename = "all_layers.txt"
	all_layers_data = open(all_layers_filename,'w')

	#Loop through number of layers
	for i in range(1,layers+1):
		all_layers_data.write("layer" + str(i) + '\n')

		print("Layer:" + str(i))		
		layer_filename = "layer_"+str(i)+".txt"
		layer = open(layer_filename,'w')		

		#Loop through each node and generate edges and weights
		for j in range(1,nodes+1):
			print("Node:" + str(j))
			edges = np.random.randint(1,nodes)
			#For each node generate edges
			for k in range(1,edges):
				weight = np.around(np.random.rand(1),1)
				layer.write(str(j) + "," + str(k) + "," + str(weight[0]) + '\n')
				all_layers_data.write(str(j) + "," + str(k) + "," + str(weight[0]) + '\n')

	layer.close()

	#Inter_layer

	for i in range(1,layers):
		all_layers_data.write("inter_layer" + str(i) + str(i+1) + '\n')
		print("InterLayer" + str(i) + str(i+1))
		inter_layer_filename = "interlayer_"+str(i)+str(i+1)+".txt"
		inter_layer = open(inter_layer_filename,'w')		

		number_of_nodes = np.random.randint(1,nodes)
		#Loop through each node and generate edges and weights
		for j in range(1,number_of_nodes):
			print("Node:" + str(j))
			edges = np.random.randint(1,number_of_nodes)
			print("Edges:" + str(edges))
			#For each node generate edges
			for k in range(1,edges):
				weight = np.around(1/edges,3)
				inter_layer.write(str(j) + "," + str(k) + "," + str(weight) + '\n')
				all_layers_data.write(str(j) + "," + str(k) + "," + str(weight) + '\n')

	inter_layer.close()


def arena_3d(layers):
	arena_file = open("D:\Downloads\Arena3D_v2.0\Arena3D_v2.0\Input Files Examples\Arena_file.txt",'w')
	arena_file.write("start_connections" + "\n")
	for i in range(1,layers+1):
		layer_name = "layer_"+str(i)
		filename = "layer_"+str(i)+".txt"
		with open(filename,'r') as graph_data:
			for line in graph_data:
				edge = line.split(',')
				weight = edge[2]
				weight = weight.split()
				arena_file.write(edge[0] + "::" + layer_name + "	" + edge[1] + "::" + layer_name + "	" + weight[0])
				arena_file.write('\n')

	for i in range(1,layers):
		inter_filename = "interlayer_"+str(i)+str(i+1)+".txt"
		from_layer = "layer_"+str(i)
		to_layer = "layer_"+str(i+1)
		with open(inter_filename,'r') as graph_data:
			for line in graph_data:
				edge = line.split(',')
				weight = edge[2]
				weight = weight.split()
				arena_file.write(edge[0] + "::" + from_layer + "	" + edge[1] + "::" + to_layer + "	" + weight[0])
				arena_file.write('\n')
	arena_file.write("end_connections")
	arena_file.close()

generate_graph_data(6,20)
arena_3d(6)