# x, y, z, n = (int(input()) for _ in range(4))
x, y, z, n = [2, 2, 2, 2]
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

pow2 = [2 ** x for x in range(10)]
print(pow2)

pow3 = [2 ** x for x in range(10) if x > 5]
print(pow3)