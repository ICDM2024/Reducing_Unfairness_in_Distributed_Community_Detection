# Reducing_Unfairness_in_Distributed_Community_Detection

HBGR is a Homphily-Based Graph Reweighting algorithm, which can be applied on different distributed community detection frameworks to enhance the fairness performance.

1. Requirements
   - Python (versions > 3.7 preferred)
   - NetworkX (network analysis in Python): https://networkx.org/
   - OpenMP should be installed
   
3. How to run:
   python HBGR.py [input_file] [input_attribute_file] [negative_weight_probability]
   Eg. python HBGR.py dataset/musae_git_edges.csv dataset/musae_git_target.csv 0.5
   
   - input_file: only support edge list file format now, will support more file formats soon.
   - input_attribute_file: format highly depends on original files, when doing test, you need be careful to change the code to read attribute from input_original_file (such as the  
     attribute index in the reading file list)
   - negative_weight_probability: [0,1] usually set it to 0.5 and could get good overall performance on fariness, but can be close to 0 (better for accuracy) or 1 (better for fairness)
   
4. How to test:
   Input (G_prime) file to distributed community detection frameworks: RelaxMap (distributed InfoMap) and METIS-Based Vite (distributed Louvain)

   - RelaxMap: https://github.com/uwescience/RelaxMap/tree/master
   - Vite: https://github.com/ECP-ExaGraph/vite
  
   For METIS-Based Vite, you need to first input G-prime into METIS, and then input the results of METIS (each partition contains a number of nodes) into the input of Vite (as the 
   nodess that need to be processed by different processors when Vite is working).
   
5. How to test:
   After get community structure (sequential version, standart distributed version and HBGR distributed version), the following tests can be performed：
   
   - Accuracy Test (modularity): https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html
   - Fairness Test: F_balance and WIR (please refer to paper)
   - Efficiency Test: Divide the running time of the sequential algorithm by the running time of the distributed algorithm. The smaller the value, the better the running efficiency 
     (RelaxMap and Vite offer total computational time). 
   
