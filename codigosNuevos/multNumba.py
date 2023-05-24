import numpy as np
from numba import jit, prange
import time
import threading

N = 256 # Tamaño de las matrices
num_threads = 2 # Número de hilos

a = np.random.rand(N,N)
b = np.random.rand(N,N)
c = np.zeros((N,N))

@jit(nopython=True, parallel=True)
def matmul(a, b, c):
    for i in prange(N):
        for j in range(N):
            c_val = 0
            for k in range(N):
                c_val += a[i,k] * b[k,j]
            c[i,j] = c_val

# Función que divide el trabajo en diferentes hilos
def thread_func(thread_id):
    start = int(thread_id * N / num_threads)
    end = int((thread_id+1) * N / num_threads)
    for i in range(start, end):
        for j in range(N):
            c_val = 0
            for k in range(N):
                c_val += a[i,k] * b[k,j]
            c[i,j] = c_val

# Inicia los hilos
threads = []
start_time = time.time()
for i in range(num_threads):
    t = threading.Thread(target=thread_func, args=(i))
    t.start()
    threads.append(t)

# Espera a que todos los hilos terminen
for t in threads:
    t.join()
end_time = time.time()

# Muestra el tiempo de ejecución
print("Tiempo de ejecución:", end_time - start_time)
