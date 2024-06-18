import networkx as nx
import random

def HBGR(nagative_random, input_file, input_attribute_file):
    n_random = nagative_random
    
    # Read graph from input file
    inputs = open(input_file, "r" )
    data = []
    G = nx.Graph()
    attribute = 1
    for line in inputs:
        number_strings = line.split() 
        numbers = [int(n) for n in number_strings] 
        data.append(numbers) 
    G = nx.Graph()
    G.add_edges_from(data)
    
    # Record total number of edges and nodes for calculating the difference between the actual number of edges
    # connecting two group (or within the same group) nodes and their expected number of edges
    total_edges = len(G.edges())
    total_nodes = len(G.nodes())
    
    # Read attribute file, and divides node into two groups: Red and Blue 
    # (Can be extended to multiple attributes)
    inputs = open(input_attribute_file, "r" )
    data = []
    blue_Group = []
    red_Group = []
    node_list = []
    attribute_list=  []
    for line in inputs:
        number_strings = line.split() 
        numbers = int(number_strings[2])
        if (numbers >= attribute):
            blue_Group.append(int(number_strings[0]))
        if (numbers < attribute):
            red_Group.append(int(number_strings[0]))
        node_list.append(int(number_strings[0]))    
        attribute_list.append(numbers)

    blue_nodes = len(blue_Group)
    red_nodes = len(red_Group)

    for i in G.nodes():
        index = node_list.index(i)
        G.nodes[i]['research'] = attribute_list[index]
    
    # Add attribute to graph G, and record real number of edges for connecting Red-Red, Blue-Blue or Red-Blue
    r_r = 0
    b_b = 0
    r_b = 0
    for i in G.edges():
        if (G.nodes[i[0]]["research"] == G.nodes[i[1]]["research"] == 0):
            r_r += 1
        if (G.nodes[i[0]]["research"] == G.nodes[i[1]]["research"] == 1):
            b_b += 1
        if (G.nodes[i[0]]["research"] != G.nodes[i[1]]["research"]):
            r_b += 1

    # Compute the probability (Real & Expected)of connecting edges from different groups (Red-Red, Blue-Blue, Red-Blue)
    Rr_r = r_r / total_edges
    Er_r = (red_nodes / total_nodes) ** 2
    Rb_b = b_b / total_edges
    Eb_b = (blue_nodes / total_nodes) ** 2
    Rr_b = r_b / total_edges
    Er_b = 2 * (blue_nodes / total_nodes) * (1 - (blue_nodes / total_nodes ))
    
    # Build new graph: G_prime with homophily-based new weight, and output G_prime to a file
    G_new = nx.Graph()
    name = "dataset/musae_git_edges.csv"
    inputs = open(name, "r" )
    output_file = 'dataset/G_prime_musae_git_edges_.txt'
    with open(output_file, 'w') as f:
        for line in inputs:
            number_strings = line.split() 
            numbers = [int(n) for n in number_strings] 
            index_node1 = node_list.index(numbers[0])
            index_node2 = node_list.index(numbers[1])
            g_random = random.uniform(0, 1)
            if (attribute_list[index_node1] != attribute_list[index_node2]):
                G_new.add_edge(numbers[0], numbers[1], weight= abs(Er_b - Rr_b))
                f.write(str(int(numbers[0])))
                f.write("\t")
                f.write(str(int(numbers[1])))
                f.write("\t")
                f.write(str(abs(Er_b - Rr_b)))
                f.write("\n")
            if (attribute_list[index_node1] == attribute_list[index_node2] == 0):
                if (g_random  > n_random):
                    G_new.add_edge(numbers[0], numbers[1], weight= abs(Er_r - Rr_r))
                    f.write(str(int(numbers[0])))
                    f.write("\t")
                    f.write(str(int(numbers[1])))
                    f.write("\t")
                    f.write(str(abs(Er_r - Rr_r)))
                    f.write("\n")
                if (g_random  <= n_random):
                    G_new.add_edge(numbers[0], numbers[1], weight= - abs(Er_r - Rr_r))
                    f.write(str(int(numbers[0])))
                    f.write("\t")
                    f.write(str(int(numbers[1])))
                    f.write("\t")
                    f.write(str(-abs(Er_r - Rr_r)))
                    f.write("\n")
            if (attribute_list[index_node1] == attribute_list[index_node2] == 1):
                if (g_random  > n_random):
                    G_new.add_edge(numbers[0], numbers[1], weight= abs(Eb_b - Rb_b))
                    f.write(str(int(numbers[0])))
                    f.write("\t")
                    f.write(str(int(numbers[1])))
                    f.write("\t")
                    f.write(str(abs(Eb_b - Rb_b)))
                    f.write("\n")
                if (g_random  <= n_random):
                    G_new.add_edge(numbers[0], numbers[1], weight= -abs(Eb_b - Rb_b))
                    f.write(str(int(numbers[0])))
                    f.write("\t")
                    f.write(str(int(numbers[1])))
                    f.write("\t")
                    f.write(str(-abs(Eb_b - Rb_b)))
                    f.write("\n")

if __name__=="__main__": 
    # Set negative random to encourage nodes from the same protected group to appear on different machines
    negative_random =  0.5
    # Set input file path
    input_file = "dataset/musae_git_edges.csv"
    input_attribute_file = "dataset/musae_git_target.csv"
    HBGR(negative_random, input_file, input_attribute_file)