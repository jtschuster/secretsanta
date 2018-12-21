from collections import defaultdict


names = [("kristen", "CR"), ("alyssa", "CR"), ("jackson", "CR"), ("tom", "CR"), ("sam", "DM"), ("sarah", "DM"), ("luke", "DM"), ("angie", "DM"), ("dave",
                                                                                                                                                  "DM"), ("pete", "DP"), ("andrea", "DP"), ("anna", "DP"), ("lauren", "DP"), ("grant", "DP"), ("grandma", "DB"), ("grandpa", "DB"), ("steve", "MI")]
names = []
groupcount = defaultdict(int)
inp = True
while inp == True:
    name = input("What is the person's name? ")
    fam = input("What group are they in? ")
    names.append((name, fam))
    groupcount[fam] += 1
    more = "x"
    while not (more == "y" or more == "n"):
        more = input("Would you like to add another person? [y/n] ")
        more = more.lower()
    if more == "y":
        inp = True
    else:
        inp = False

if max(groupcount.values()) > len(groupcount.keys()) / 2:
    print("Cannot create a workable exchange: one group is too large to not have another person in their group")
else:
    names.sort()
    names_sorted = [names[0]]
    for num in range(1, len(names)-1):
        last_in_sorted = names_sorted[len(names_sorted)-1]
        ind = num
        while last_in_sorted[1] == names[ind][1]:
            ind += 1
        names_sorted.append(names[ind])

    print(names_sorted[len(names_sorted) - 1]
          [0] + " has " + names_sorted[0][0])
    for ind in range(len(names_sorted) - 1):
        print(names_sorted[ind][0] + " has " + names_sorted[ind+1][0])
