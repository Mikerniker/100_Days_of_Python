# CODING EXERCISE
# Create your own decorator

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator():
    pass

def fast_function():
    for i in range(10000000):
        i * i
        
def slow_function():
    for i in range(100000000):
        i * i
