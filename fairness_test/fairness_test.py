import matplotlib.pyplot as plt

def fairness_test(community_structure,  input_attribute_file, attribute):
    # record number of nodes in every single community
    number_of_elements_in_Community = []
    distributed_community = community_structure
    for i in range (0,len(distributed_community)):
        print(distributed_community[i])
        number_of_elements_in_Community.append(len(distributed_community[i]))

    # calculate original distribution of Red (or Blue) group nodes 
    inputs = open(input_attribute_file, "r" ,encoding='latin-1')
    group_Red = 0
    group_Blue = 0
    total_nodes = 0
    #import re
    for line in inputs:
        str_list = line.split()
        if int(str_list[1]) >= attribute:
            group_Red+= 1
        else:
            group_Blue += 1
        total_nodes = total_nodes + 1
    OriginalDistribution = group_Red/total_nodes
    
    # traverse every cluster, record distribution of Red (or Blue) group nodes
    group_Red_distribution = []
    group_Blue_distribution = []
    for i in distributed_community:
            group_Red = 0
            group_Blue = 0
            nodes_in_Community = 0
            for j in i:
                ins = open(input_attribute_file, "r" ,encoding='latin-1')
                for line in ins:
                    str_list = line.split()
                    if str_list[0] == str(j):
                        if int(str_list[1]) >= attribute:
                            group_Red+= 1
                        else:
                            group_Blue += 1
                nodes_in_Community = nodes_in_Community + 1
            group_Red_distribution.append(group_Red/nodes_in_Community)
            group_Blue_distribution.append(group_Blue/nodes_in_Community)

    # record gap between original distribution (Red or Blue group) and community distribution (Red or Blue group)       
    gap_group_Red = []
    for i in group_Red_distribution:
        gap_group_Red.append(abs(i-OriginalDistribution))
    
    # record Fairness evaluation values based on different threshold selections
    Fairness = [] 
    for threshold in range (1,20,1):
        balance = 0
        threshold = threshold / 100
        for i in range(0,len(gap_group_Red)):
            if (gap_group_Red[i] <= threshold):
                balance += 0 * (number_of_elements_in_Community[i] / total_nodes)
            else: 
                balance += (abs(gap_group_Red[i] - threshold) ) * (number_of_elements_in_Community[i] / total_nodes)
        Fairness.append(balance)
    return Fairness

if __name__=="__main__": 
    # Obtain different community structure by using standard distributed / HBGR-Based distributed CD algorithms
    distributed_community = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12]]
    HBGR_community = [[1,3,4,6,7,10,12], [2,5], [8,9,11]]

    # Path of input attribute file
    input_attribute_file = "attribute_file/attribute.txt"

    # Set testing attribute, such as gender, race, age, residence ...
    attribute = 1

    # Evaluate fairness performance for different community structures
    fairness_distributed = fairness_test(distributed_community,  input_attribute_file, attribute)
    fairness_HBGR = fairness_test(HBGR_community,  input_attribute_file, attribute)

    # Draw Figure to show differnece on fairness performance for different community structures
    x = []
    for i in range(1,20,1):
        x.append(i)
        i+=1
    y1 = fairness_distributed
    y2 = fairness_HBGR
    plt.plot(x, y1 )
    plt.plot(x, y2, '-.')
    plt.legend(["Vite", "HBGR-Vite"], fontsize="15", loc ="upper right")
    plt.xlabel("Thresholds",fontsize=20)
    plt.ylabel("WIR (lower is better)",fontsize=20)
    plt.tick_params(labelsize=14)
    plt.title('Fariness Comparison',fontsize=20)
    plt.savefig('fairness-comparison.png', dpi=300)
    plt.show()