import numpy as np

1# P is a set of pairs (aka tuples) , mayber ordered later
def Incremental(P: set[tuple[int, int]]):
    # step 1 : sort by x
    P_sorted = tuple(sorted(P, key=lambda x: x[0]))
    print(f"{P_sorted}")

    # step 2 : create L_upp and add p1 and p2
    L_upp : list[tuple[int,int]] = []
    L_upp.append([P_sorted[0],P_sorted[1]])
    print(f"{L_upp}")

    # step 3 : Add points to L_upp , remove the second last when the turn is left
    for i in range(3, len(P)): 
        L_upp.append(P_sorted[i])
        matrix = np.array([[1,P_sorted[i-2][0],P_sorted[i-2][1]]
                           [1,P_sorted[i-1][0],P_sorted[i-1][1]],
                           [1,P_sorted[i][0],P_sorted[i][1]]
                           ])

        det = matrix.linealg.det(matrix)
        if det > 0 and len(P_sorted) -1 > : 





P = set([(10,9), (5,6), (7,8)])
Incremental(P)