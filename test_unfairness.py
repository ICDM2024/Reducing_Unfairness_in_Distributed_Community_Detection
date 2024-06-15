# get the community result for original file

import networkx as nx
import community
import numpy as np

Name = "metis_output/princeton_sequential"

ins = open(Name, "r" )
data = []

number_of_community = 0
authors = []
count = 1
for line in ins:
    authors.append(count)
    count+=1
    number_strings = line.split() # Split the line on runs of whitespace
    numbers = [int(n) for n in number_strings] # Convert to integers
    if (numbers[0]>number_of_community):
        number_of_community = numbers[0]
    data.append(numbers[0]) # Add the "row" to your list.
parallel_community = []
for i in range(0,number_of_community+1):
    parallel_community.append([])
print(parallel_community)
print(len(data))
for i in range(0,len(data)):
    #print(data[i])
    parallel_community[data[i]].append(authors[i])
