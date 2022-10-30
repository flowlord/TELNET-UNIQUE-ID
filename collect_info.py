import subprocess
from hashlib import sha3_512
import psutil
import platform

def geolocalisation():
    return  str(subprocess.run('curl ipinfo.io'))

def others():
    uname = str(platform.uname())
    svmem = str(psutil.virtual_memory())
    partitions = str(psutil.disk_partitions())

    return uname+svmem+partitions





