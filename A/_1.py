
from math  import *
from re import M
import numpy as np

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def SolveDivideAndConquer(P : list[tuple[int, int]]):
    # step 1 : x sort P  
    P_sorted = sorted(P, key=lambda x : [x[0], x[1]])
    return DivideAndConquer(P_sorted)

def DivideAndConquer(P : list[tuple[int, int]]) :
    # a flag in order to sort the first iteration
    if len(P) <= 3 :
        return CCWSorting(P) 
    
    mid = len(P) // 2
    A : list[tuple[int , int]] = P[:mid]
    B : list[tuple[int , int]] = P[mid:]

    L = DivideAndConquer(A)
    R = DivideAndConquer(B)

    return MyMerge(L,R, UppBridge(L,R), DownBridge(L,R))

# CCW sorting
def CCWSorting(P : list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(P) <= 2: 
        return list(P)


    det = ComputeDet(P[0], P[1], P[2])
    if det > 0 :
        return list(P) 

    if det == 0:
        return [P[0], P[-1]] 
    
    return [P[0], P[2], P[1]]

# Upp bridge and Down bridge for Devide And conquer
def UppBridge(A : list[tuple[int, int]], B : list[tuple[int, int]]) -> list[tuple[int, int]]:
    # step 1 : A(i) -> the far right of KP(A) , B(j) -> the far left of KB(B)
    i = len(A) - 1 
    j = 0 

    while True:
        inew = i
        jnew = j
        
        # step 2 : compute next index of A, compute dets , if * < 0 -> not in the same -> i = i_next
        i_next = (i + 1) % len(A)
        detA = ComputeDet(A[i], A[i_next], B[j])
        if detA < 0 or (detA == 0 and DistSq(A[i_next], B[j]) > DistSq(A[i], B[j])):
            inew = i_next
        

        # step 3 : same  as step 2 but with backwards
        j_prev = (j - 1) % len(B)
        detB = ComputeDet(B[j], B[j_prev], A[i])
        if detB > 0 or (detB == 0 and DistSq(B[j_prev], A[i]) > DistSq(B[j], A[i])): 
            jnew = j_prev                

        # step 4 : break condition
        if i != inew or j != jnew :
            i = inew
            j = jnew
            continue

        return [A[i],B[j]]

def DownBridge(A : list[tuple[int, int]], B : list[tuple[int, int]]) -> list[tuple[int, int]]:
    # step 1 : A(i) -> the far right of KP(A) , B(j) -> the far left of KB(B)
    i = len(A) - 1 
    j = 0 

    while True:
        inew = i
        jnew = j
        
        # step 2 : compute next index of A, compute dets , if * < 0 -> not in the same -> i = i_next
        i_prev = (i - 1) % len(A)
        detA = ComputeDet(A[i], A[i_prev], B[j])
        if detA > 0 or (detA == 0 and DistSq(A[i_prev], B[j]) > DistSq(A[i], B[j])):
            inew = i_prev

        j_next = (j + 1) % len(B)
        detB = ComputeDet(B[j], B[j_next], A[i])
        if detB < 0 or (detB == 0 and DistSq(B[j_next], A[i]) > DistSq(B[j], A[i])):
            jnew = j_next
       
        # step 4 : break condition
        if i != inew or j != jnew :
            i = inew
            j = jnew
            continue

        return [A[i],B[j]]



def MyMerge(L : list[tuple[int, int]], R : list[tuple[int, int]], upp : list[tuple[int, int]], down : list[tuple[int, int]]) -> list[tuple[int, int]]:
    i_upp = L.index(upp[0])
    j_upp = R.index(upp[1])
    i_down = L.index(down[0])
    j_down = R.index(down[1])
    
    idx = i_upp 
    Merged = []
    while True:
        Merged.append(L[idx])
        if (idx == i_down):
            break
        idx = (idx + 1) % len(L)

    idx = j_down
    while True:
        Merged.append(R[idx])
        if (idx == j_upp):
            break
        idx = (idx + 1) % len(R)

    return Merged

def ComputeDet(x : tuple[int, int], y : tuple[int, int], z : tuple[int, int]) -> int:
    x1,y1 = x 
    x2,y2 = y 
    x3,y3 = z 

    det = x2*y3 - x3*y2 -x1*y3 + x1*y2 + y1*x3 - y1*x2
    return det

# to check sinefthiaka kai katheta 
def DistSq(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2  

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def SolveQuickHull(P : list[tuple[int, int]]) -> list[tuple[tuple, tuple]]:
    ax = max(P, key= lambda x : x[0]) 
    ay = max(P, key= lambda x : x[1]) 
    bx = min(P, key= lambda x : x[0]) 
    by = min(P, key= lambda x : x[1]) 

    BxBy = findRight(bx, by, P)
    ByAx = findRight(by, ax, P)
    AxAy = findRight(ax, ay, P)
    AyBx = findRight(ay, bx, P)

    return QuickHull(bx, by, BxBy) + QuickHull(by, ax, ByAx) + QuickHull(ax, ay, AxAy) + QuickHull(ay, bx, AyBx)

def QuickHull(A : tuple[int, int], B : tuple[int, int], S : list[tuple[int , int]]) -> list[tuple[int, int]]:
    if len(S) == 2 :
        return [A,B]
    
    G = findMaxDist(A,B,S)
    M = findRight(A,G,S)
    N = findRight(G,B,S)

    return QuickHull(A,G,M), QuickHull(G,B,N)


def findRight(A : tuple[int, int], B : tuple[int ,int], S : list[tuple[int , int]]) -> list[tuple[int ,int]]:
    RightList = []
    for point in S: 
        det = ComputeDet(A, B, point)
        if det < 0:
            RightList.append(point)


    return RightList