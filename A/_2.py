from _1 import *
import matplotlib.pyplot as plt
import random

P = [] 
for _ in range(150):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    P.append((x,y))

px,py =  zip(*P)
# blue dots
plt.scatter(px,py, color='blue', s=15, label='Starting points')

# Incremental resutlts
incremental = Incremental(P)
# finish the circle
incremental.append(incremental[0])
ix, iy = zip(*incremental)
plt.plot(ix,iy, color='red',linewidth=2 ,label='Incremental')

plt.title("Incremental")
plt.legend()
plt.show()



# Gift wrapping resutlts
gift = GiftWrapping(P)
# finish the circle
gift.append(gift[0])
ix, iy = zip(*gift)

plt.scatter(px,py, color='blue', s=15, label='Starting points')
plt.plot(ix,iy, color='green',linewidth=2 ,label='Gift Wrapping')

plt.title("Gift Wrapping")
plt.legend()
plt.show()


# Devide and Conquer result
dnq = SolveDivideAndConquer(P)
dnq.append(dnq[0])
dx,dy = zip(*dnq)

plt.scatter(px,py, color='blue', s=15, label='Starting Points')
plt.plot(dx,dy,color= 'yellow', linewidth=2, label='Devide and Conquer')

plt.title("Devide and Conquer")
plt.legend()
plt.show()

# Quick hull 

quick = SolveQuickHull(P)
quick.append(quick[0])
qx,qy = zip(*quick)

plt.scatter(px, py, color='blue', label='Starting Points')
plt.plot(qx, qy, linewidth=2, label='Quick Hull')

plt.title("Quick hull")
plt.legend()
plt.show()


