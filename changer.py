import os
import sys
print('1. change mtu value')
print('2. restore mtu value')
argv = sys.argv[1]
if(argv==1):
    os.system("sudo ifconfig en0 mtu 471")
else:
    os.system("sudo ifconfig en0 mtu 1500")