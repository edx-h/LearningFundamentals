from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from time import sleep

def factorial(n: int): 
    sleep(1E-3)

    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def callback(future: Future):
    print(future.result())

pool = ThreadPoolExecutor(3)

for i in range(1, 7):
    exec(f'future_{i} = pool.submit(factorial, i)')
    exec(f'future_{i}.add_done_callback(callback)')
