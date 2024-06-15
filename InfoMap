import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import time

start = time.perf_counter()
#inname = inname = "3brandeis99"
Name =  "large_twitch_edges.csv"
ins = open(Name, "r" )
data = []

from infomap import Infomap

# Command line flags can be added as a string to Infomap
im = Infomap("--two-level --directed")

# Add weight as optional third argument
#im.add_link(0, 1)

for line in ins:
    number_strings = line.split() # Split the line on runs of whitespace
    numbers = [int(n) for n in number_strings] # Convert to integers
    data.append(numbers) # Add the "row" to your list.
    print(numbers)
    im.add_link(numbers[0], numbers[1])
#print(data) # [[1, 3, 4], [5, 5, 6]]
#print (data)
G = nx.Graph()
# add edges from txt 
G.add_edges_from(data)
