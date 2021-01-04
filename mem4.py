from __future__ import print_function
import psutil
import time


def allocate_memory():
    t_end = time.time() + 60 * 1
    while time.time() < t_end:
        # print(psutil.cpu_percent())
        print(psutil.virtual_memory()) # physical memory usage
        print('total memory:', psutil.virtual_memory()[0])
        print('memory % used:', psutil.virtual_memory()[2])
        print('used:', psutil.virtual_memory()[3])
        print('free memory:', psutil.virtual_memory()[4])
        mem_req = 6813351936-psutil.virtual_memory()[3]
        print(mem_req)
        bytearray(mem_req)


allocate_memory()
