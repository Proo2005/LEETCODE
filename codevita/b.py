import numpy as np
import pandas as pd
def area(v):
    x=[a[0] for a in v]
    y=[a[1] for a in v]
    return 0.5 * abs(sum(x[i] * y[(i + 1) % len(y)] - x[(i + 1) % len(x)] * y[i] for i in range(len(x))))

n=int(input())
v=[]
for i in range(n):
    a,b=map(int,input().split())
    v.append((a, b))

print(area(v))