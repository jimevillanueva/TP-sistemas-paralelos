from numba import njit, set_num_threads, jit, prange,  get_num_threads
import threading
import timeit

N = 4096
threads = 8
A = [1 for x in range(N*N)]  
B = [2 for x in range(N*N)]
C = [0 for x in range(N*N)]

@jit(nopython=True, parallel=True)
def mult():
  for i in prange(N):
      posi = i * N
      for j in range(N):
          posj = j * N
          mult=0
          for k in range(N):
              mult = A[posi + k] * B[posj + k]
          C[posi + j] = mult

set_num_threads(threads)

thr = []

for i in range(threads):
    thr.append(threading.Thread(target=mult))

start = timeit.default_timer()
for i in range(threads):
    thr[i].start()

for i in range(threads):
    thr[i].join()

stop = timeit.default_timer()
print( stop - start) 