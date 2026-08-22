from _1 import *
import random

P = [] 
for _ in range(150):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    P.append((x,y))

print(f"150 Radom points : {P}")
print("-" * 50)
print(f"Incremental: {Incremental(P)}")
print("-" * 50)
print(f"Gift Wrapping: {GiftWrapping(P)}")
print("-" * 50)
print(f"Devide and Conquer: {SolveDivideAndConquer(P)}")
print("-" * 50)
print(f"Quick Hull: {SolveQuickHull(P)}")




    


