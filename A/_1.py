import numpy as np

# P is a set of pairs (aka tuples) , mayber ordered later
def Incremental(P: set[tuple[int, int]]):
    # step 1 : sort by x
    P_sorted = tuple(sorted(P, key=lambda x: x[0]))

    # step 2 : create L_upp and add p1 and p2
    L_upp : list[tuple[int,int]] = []
    L_upp.append(P_sorted[0])
    L_upp.append(P_sorted[1])

    # step 3 : Add points to L_upp , remove the second last when the turn is left
    for i in range(2, len(P)): 
        L_upp.append(P_sorted[i])

        while (len(L_upp) > 2):

            # create matrix  [ 1 x1 y1 ] 
            #                [ 1 x2 y2 ]
            #                [ 1 x3 y3 ]

            # det = 1 * [x2 y2] - x1 * [1 y2] + y1 [1 x2]
            #           [x3 y3]        [1 y3] +    [1 x3]

            # det = x2y3 - x3y2 -x1y3 + x1y2 + y1x3 - y1x2
            
            x1 = L_upp[-3][0]
            y1 = L_upp[-3][1]
            x2 = L_upp[-2][0]
            y2 = L_upp[-2][1]
            x3 = L_upp[-1][0]
            y3 = L_upp[-1][1]


            det = x2*y3 - x3*y2 -x1*y3 + x1*y2 + y1*x3 - y1*x2

            if det >= 0:
                L_upp.pop(-2)
            else:
                break


    # step 4 : create L_down add p_(i-1) and p_(i)
    L_down : list[tuple[int, int]] = []
    L_down.append(P_sorted[-1])
    L_down.append(P_sorted[-2])

    # set 5 : add to L_down till only two points left or there is a right 
    for j in range(len(P_sorted) - 3, -1, -1):
        L_down.append(P_sorted[j])

        while (len(L_down) > 2):
            x1,y1 = L_down[-3]
            x2,y2 = L_down[-2]
            x3,y3 = L_down[-1]

            det = x2*y3 - x3*y2 -x1*y3 + x1*y2 + y1*x3 - y1*x2

            if det >= 0:
                L_down.pop(-2)
            else:
                break

    # step 6 : remove first and last element
    L_down.pop(-1)
    L_down.pop(0)

    L = L_upp + L_down
    return L