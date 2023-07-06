from time import time

N = 512

A = [1 for x in range(N*N)]  
B = [1 for x in range(N*N)] 
C = [0 for x in range(N*N)]

start = time()

for i in range(N):
    posi = i * N
    for j in range(N):
        posj = j * N
        mult = 0
        for k in range(N):
            mult += A[posi + k] * B[posj + k]
        C[posi + j] = mult

stop = time()
print("Tiempo de ejecución:", stop - start) 
