import threading
import timeit

N = 2048
threads = 4
A = [1 for x in range(N*N)]  
B = [2 for x in range(N*N)] 
C = [0 for x in range(N*N)]

def mult(id):
    desde = int((N/threads)*id)
    hasta = int(desde + (N/threads))
    for i in range(desde,hasta):
        posi = i * N
        for j in range(N):
            posj = j * N
            mult=0
            for k in range(N):
                mult += A[posi + k] * B[posj + k]
            C[posi + j] = mult

thr = []
for i in range(threads):
    thr.append(threading.Thread(target=mult, args=[i]))

start = timeit.default_timer()

for i in range(threads):
    thr[i].start()

for i in range(threads):
    thr[i].join()

stop = timeit.default_timer()
print( stop - start) 