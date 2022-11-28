import platform, psutil


System = platform.uname()

print(f"System: {System.system}")
print(f"Node Name: {System.node}")
print(f"Release: {System.release}")
print(f"Version: {System.version}")
print(f"Machine: {System.machine}")
print(f"Processor: {System.processor}")

print(f"Memory :{psutil.virtual_memory()}")
print("cpu pourcent",psutil.cpu_percent(4))

import os
os.system(cmd)