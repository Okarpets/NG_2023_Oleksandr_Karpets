import psutil
import socket
from platform import uname
import os
print("Please wait for end of library installing")
os.system('python -m pip install psutil\npython -m pip install socket')
print("Your system: " + uname().system, uname().release)
print("Your PC name: " + uname().node)
print("Proccesor name:" + uname().processor)
print("Number of processor cores: " + str(psutil.cpu_count(logical=True)))
print("CPU frequency (Rec, Min, Max): " + str(psutil.cpu_freq()))
print("RAM size:" + str(psutil.virtual_memory().total))
print("RAM size you can use now:" +  str(psutil.virtual_memory().available))
print("RAM size what you use now:" + str(psutil.virtual_memory().used))
print("Machine architecture:" + uname().machine)
print("Your ip address: " + socket.gethostbyname(socket.gethostname()))