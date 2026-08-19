import numpy as np
from math import floor, ceil

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
            
            x1,y1 = L_down[-3]
            x2,y2 = L_down[-2]
            x3,y3 = L_down[-1]

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

def GiftWrapping(S : set[tuple[int , int]]):
    # step 1 : r = min(S)
    r = r0 = min(S, key=lambda x: (x[0], x[1])) 
    #print(f"R0 : {r0}")

    # step 2 : create the chain
    Chain : list[tuple[int , int]] = [r0]

    # step 3 : select a u (different of r), then select a t (different from u and r) if u closer right than t then u = t
    while True:
        u = next(point for point in S if point != r)
        for t in S:
            if t == u or t == r : continue 
            # if clockwise or sinefthiaka -> det <= 0  
            
            x1,y1 = r
            x2,y2 = u 
            x3,y3 = t

            det = x2*y3 - x3*y2 -x1*y3 + x1*y2 + y1*x3 - y1*x2

            if det < 0 : 
                u = t
            elif det == 0 :
                # sinefthiaka , ypologizoume thn apostash r->u kai r->t. An ru < rt then u = t
                distance_ru = (x2 - x1)**2 + (y2 - y1)**2       
                distance_rt = (x3 - x1)**2 + (y3 - y1)**2       
                if distance_ru < distance_rt :
                    u = t

        # step 4 : end of the loop . Chain finished
        if u == r0:
            break
        
        r = u
        Chain.append(r)

    return Chain
def SolveDevideAndConquer(P : set[tuple[int, int]]):
    # step 1 : x sort P  
    P_sorted = tuple(sorted(P, key=lambda x : [x[0], x[1]]))
    return DivideAndConquer(P_sorted)

def DivideAndConquer(P : set[tuple[int, int]]):
    # a flag in order to sort the first iteration
    if len(P) <= 3 :
        return CCWSorting(P) 

    A : set[tuple[int , int]] = P[0 : ceil(len(P)/2)]
    B : set[tuple[int , int]] = P[floor (len(P)/2) + 1 : len(P)]
    print(f"P : {P}")
    print(f"A : {A}")
    print(f"B : {B}")
#    DivideAndConquer(A) 
#    DivideAndConquer(B)
    UppBridge(A,B)
    DownBridge(A,B)

    return
# CCW sorting
def CCWSorting(P : set[tuple[int, int]]):
    return
# Upp bridge and Down bridge for Devide And conquer
def UppBridge(A : set[tuple[int, int]], B : set[tuple[int, int]]):
    return

def DownBridge(A : set[tuple[int, int]], B : set[tuple[int, int]]):
    return


S = set([(10,27), (5,6), (7,8), (0,2), (2,5)])
SolveDevideAndConquer(S)

