import numpy as np

# Airship Fortress	0
# Shy Guy Bazzar	1
# Desert Hills	2
# Bowser's Castle	3
# Wario Stadium	4
# Mario bros Circuit	5
# Whistlestop Summit	6
# Dry Bones Burnout	7
# Toad's Factory	8
# Choco Mountain	9
# Crown City	10
# DK Spaceport	11
# Acorn Heights	12
# Mario Circuit	13
# Moo Moo Meadows	14
# Peach Stadium	15
# Koopa Troopa Beach	16
# Boo Cinema	17
# Dandelion Depths	18
# Cheep Cheep Falls	19
# Faraway Oasis	20
# Dino Dino Jungle	21
# Star View Peak	22
# DK Pass	23
# Salty Salty Speedway	24
# Great ? Block Ruins	25
# Sky High Sundae	26
# Wario Shipyard	27
# Peach Beach	28
# Rainbow Road    29


# Adjacency matrix
A = np.array([
[0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],


])

# Calculate the number of paths of length 6 (5 sides)
def count_simple_paths(A):
    n = A.shape[0]
    paths = 0

    for n1 in range(n):
        for n2 in range(n):
            if A[n1, n2] == 1:
                for n3 in range(n):
                    if A[n2, n3] == 1 and n3 != n1:
                        for n4 in range(n):
                            if A[n3, n4] == 1 and n4 != n2 and n4 != n1:
                                for n5 in range(n):
                                    if A[n4, n5] == 1 and n5 != n3 and n5 != n2 and n5 != n1:
                                        for n6 in range(n):
                                            if A[n5, n6] == 1 and n6 != n4 and n6 != n3 and n6 != n2 and n6 != n1:
                                                paths += 1
    return paths

print("Total paths of length 6:", count_simple_paths(A))
