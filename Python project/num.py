import numpy as np 
import time 
size =100000000
py_list= list(range(size))
start = time.time()
end = time.time()
print(f"python list = {start-end}")
np_arr = np.array(py_list)