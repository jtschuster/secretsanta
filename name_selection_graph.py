from collections import defaultdict
import random

names = [("kristen", "CR"), ("alyssa", "CR"), ("jackson", "CR"), ("tom", "CR"), ("sam", "DM"), ("sarah", "DM"), ("luke", "DM"), ("angie", "DM"), ("dave",
                                                                                                                                                  "DM"), ("pete", "DP"), ("andrea", "DP"), ("anna", "DP"), ("lauren", "DP"), ("grant", "DP"), ("grandma", "DB"), ("grandpa", "DB"), ("steve", "MI")]
justnames = []  # has a list of names used for choosing at random
for name in names:
    justnames.append(name[0])

# a hash table with names as a key and a list of people they can't have as the value
# represents a graph where people already have themselves and anyone in their family
adjacency_list = {}

for name in names:  # populated the graph with data from the names array of tuples
    li = []
    for name2 in names:
        if name2[1] == name[1]:
            li.append(name2[0])
    adjacency_list[name[0]] = li


# a hashtable with sizes of groups as the keys and names as the values - used to order those in the largest groups/families first
group_sizes = defaultdict(list)
for name in adjacency_list.keys():
    size = len(adjacency_list[name])
    group_sizes[size].append(name)

# list of sizes of families to
group_sizes_list = sorted(group_sizes, reverse=True)

keyhasgotval = {}  # to hold the final picks of who has who
for size in group_sizes_list:  # picks who has who, starting with those in the largest groups going to the smallest
    # for each group size, go through the names of those in those group sizes
    for name in group_sizes[size]:
        # randomly assign it a name from the justname array (should be renamed namehat)
        namehas = justnames[random.randrange(len(justnames))]
        #print(name + " has " + namehas)
        # change the name if it appears in the list of names he can't have
        while (namehas in adjacency_list[name]):
            namehas = justnames[random.randrange(len(justnames))]
            #print(name + " has " + namehas)
        # once we found a name that works, remove name from hat
        justnames.remove(namehas)
        # key is person, value is who they have, or could be the other way, doesn't actually matter
        keyhasgotval[name] = namehas

for key, val in keyhasgotval.items():
    print(key + " has " + val)
