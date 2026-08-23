# a drone will have to find grounad targets 
# convex hull will help to track the minimal range in order to  include all targes dealing maximum damage (by bomb) 
# Then knowing the radius of a bomb will calculate the minimum amount of bombs in order to 
# include all targets

import random
import matplotlib.pyplot as plt

rad = 20
# ----------------QUICK HULL--------------------------
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
    if len(S) == 0 :
        return [A]
    
    G = findMaxDist(A,B,S)
    M = findRight(A,G,S)
    N = findRight(G,B,S)

    return QuickHull(A,G,M) + QuickHull(G,B,N)


def findMaxDist(A : tuple[int, int], B : tuple[int, int], S : list[tuple[int , int]]) -> tuple[int, int]:
    max_point = ()
    maximum = -1

    for point in S:
        det = ComputeDet(A, B, point)
        if abs(det) > maximum :
            maximum = abs(det)
            max_point = point

    return max_point    

def findRight(A : tuple[int, int], B : tuple[int ,int], S : list[tuple[int , int]]) -> list[tuple[int ,int]]:
    RightList = []
    for point in S: 
        det = ComputeDet(A, B, point)
        if det < 0:
            RightList.append(point)


    return RightList

def ComputeDet(x : tuple[int, int], y : tuple[int, int], z : tuple[int, int]) -> int:
    x1,y1 = x 
    x2,y2 = y 
    x3,y3 = z 

    det = x2*y3 - x3*y2 -x1*y3 + x1*y2 + y1*x3 - y1*x2
    return det
#--------------------------------------------------------------------------

targets = [(random.randint(1,100),random.randint(1,100)) for _ in range(1,21)]
quick = SolveQuickHull(targets)
quick.append(quick[0])
tx,ty = zip(*targets)
qx,qy = zip(*quick)

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(tx, ty, color='red', s=25, zorder=5, label='Ground Targets')
ax.plot(qx, qy, color='blue', linewidth=2, label='Minimal Target Area (Convex Hull)')

bomb_centers = quick  # Τοποθέτηση στις ακραίες κορυφές

for i, (bx, by) in enumerate(bomb_centers):
    # Σχεδιασμός κύκλου έκρηξης
    circle = plt.Circle(
        (bx, by),
        rad,
        color='orange',
        alpha=0.2,
        ec='darkorange',
        linestyle='--',
    )
    ax.add_patch(circle)
    # Κέντρο βόμβας
    ax.scatter(
        bx,
        by,
        color='orange',
        marker='x',
        s=50,
        zorder=6,
        label='Bomb Detonation Center' if i == 0 else "",
    )

ax.set_aspect('equal')  # Για να φαίνονται οι κύκλοι στρογγυλοί και όχι αυγά
plt.title(
    f"Drone Strike Coverage: {len(bomb_centers)} Bombs (Radius={rad}) for Convex Hull Targets"
)

plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend(loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()



