import threading
from time import time

N = 1024
threads =1
A = [1 for _ in range(N*N)]  
B = [1 for _ in range(N*N)] 
C = [0 for _ in range(N*N)]

def mult(desde, hasta):
    for i in range(desde, hasta):
        posi = i * N
        for j in range(N):
            posj = j * N
            mult = 0
            for k in range(N):
                mult += A[posi + k] * B[posj + k]
            C[posi + j] = mult

thr = []
for i in range(threads):
    desde = int((N / threads) * i)
    hasta = int(desde + (N / threads))
    thr.append(threading.Thread(target=mult, args=(desde, hasta)))

start = time()

for i in range(threads):
    thr[i].start()

for i in range(threads):
    thr[i].join()

stop = time()
print( stop - start) 
