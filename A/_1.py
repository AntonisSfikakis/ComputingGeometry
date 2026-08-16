import numpy as np

1# P is a set of pairs (aka tuples) , mayber ordered later
def Incremental(P: set[tuple[int, int]]):
    # step 1 : sort by x
    P_sorted = tuple(sorted(P, key=lambda x: x[0]))
    print(f"{P_sorted}")

    # step 2 : create L_upp and add p1 and p2
    L_upp : list[tuple[int,int]] = []
    L_upp.append(P_sorted[0])
    L_upp.append(P_sorted[1])
    print(f"{L_upp}")

    print(f"{len(P_sorted)}")
    # step 3 : Add points to L_upp , remove the second last when the turn is left
    for i in range(2, len(P)): 
        L_upp.append(P_sorted[i])

        while (len(L_upp) > 2):

            # create matrix  [ 1 x1 y1 ] 
            #                [ 1 x2 y2 ]
            #                [ 1 x3 y3 ]

            # det = 1 * [x2 y2] - x1 * [1 y2] + y1 [1 x2]
            #           [x3 y3]        [1 y3] +    [1 x3z]
            matrix = np.array([[1,L_upp[-3][0],L_upp[-3][1]],
                               [1,L_upp[-2][0],L_upp[-2][1]],
                               [1,L_upp[-1][0],L_upp[-1][1]]
                            ])

            det = np.linalg.det(matrix)
            # the  middle of the three is the last of L_upp  (p_(i-1))
            if det >= 0:
                L_upp.pop(-2)
            else:
                break

    print(f"RESULT : {L_upp}")

    # step 4 : create L_down add p_(i-1) and p_(i)
    L_down : list[tuple[int, int]] = []
    L_down.append(P_sorted[-2])
    L_down.append(P_sorted[-1])
    print(f"{L_down}")

    print("LOOP STARTS")
    for j in range(len(P_sorted) - 3, -1, -1):
        print(f"{P_sorted[j]}")


P = set([(10,27), (5,6), (7,8), (0,2), (2,5)])
Incremental(P)