from _1 import *
import random
from tabulate import tabulate
import time

sizes = [100, 1000 , 5000, 10000, 100000, 1000000]
table_data = []

headers = [
    "N Points",
    "Incremental (s)",
    "Gift Wrap (s)",
    "D&C (s)",
    "QuickHull (s)",
]

for s in sizes:
    P = [(random.randint(0,10000),  random.randint(0,10000)) for _ in range(s)]

    t0 = time.time()
    Incremental(P)
    t_end = time.time()
    ti = t_end - t0

    t0 = time.time()
    GiftWrapping(P)
    t_end = time.time()
    tg = t_end - t0

    t0 = time.time()
    SolveDivideAndConquer(P)
    t_end = time.time()
    td = t_end - t0

    t0 = time.time()
    SolveQuickHull(P)
    t_end = time.time()
    ts = t_end - t0

    table_data.append([s, f"{ti:.6f}", f"{tg:.6f}", f"{td:.6f}", f"{ts:.6f}"])

print(tabulate(table_data, headers=headers, tablefmt = "fancy grid"))

    