import numba
import numpy as np
import time
import os

os.environ['NUMBA_THREADING_LAYER'] = 'threadpool'

N = 512  # Tamaño de las matrices
threads= 2 # Cantidad de hilos
numba.set_num_threads(threads) 

# Declaracion de los vectores
a = np.random.rand(N*N)
b = np.random.rand(N*N)
c = np.zeros(N*N)

def printArray(arr):        
    print('{', end='')
    for i in range (N):
        if (i>0):
            print()
        for j in range (N):
            print('['+str(arr [i*N+j])+']', end='')
    print('}')

# Funcion que resuelve la multiplicacion
@numba.jit(nopython=True, parallel=True)
def thread_func(c):
    for i in numba.prange(N):
        auxi= i*N
        for j in range(N):
            auxj= j*N
            c_val = 0.0
            for k in range(N):
                c_val += a[auxi+k] * b[auxj + k]
            c[auxi+j] = c_val

start_time = time.time()
thread_func(c)
end_time = time.time()

# Muestra el tiempo de ejecución
print("Tiempo de ejecución:", end_time - start_time)
