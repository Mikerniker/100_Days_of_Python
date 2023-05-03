# CODING EXERCISE
# Create your own decorator

import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def run_speed():
       start_time = time.time()
       function
       end_time = current_time
       difference = start_time - end_time
       print(f"{function.__name__} run speed: {difference}")
    return run_speed

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()