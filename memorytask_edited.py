import psutil
import time
# import ctypes, tempfile
# from ctypes import *

def allocate_memory():
    t_end = time.time() + 60 * 1
    while time.time() < t_end:
        print(psutil.cpu_percent())
        print(psutil.virtual_memory())  # physical memory usage
        print('total memory:', psutil.virtual_memory()[0])
        print('memory % used:', psutil.virtual_memory()[2])
        print('used:', psutil.virtual_memory()[3])
        print('free memory:', psutil.virtual_memory()[4])
        eighty_percent = 0.8 * psutil.virtual_memory()[0]
        print('80% of total memory = ', eighty_percent)
        mem_req = eighty_percent - psutil.virtual_memory()[3]
        print('memory to be added= ', mem_req)
        split_mem_req = str(mem_req).split('.')
        int_part = int(split_mem_req[0])
        decimal_part = int(split_mem_req[1])
        print ('int= ', int_part)
        print ('decimal= ', decimal_part)
        if int_part<=0:
            break

        x = bytearray(int_part)

        time.sleep(2.0)

allocate_memory()