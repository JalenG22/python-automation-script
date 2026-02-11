#System Info File#

import platform 
import os 

print("System Information")
print("---------")
print(f"OS: {platform.system()} {platform.release()}")
print(f"CPU Cores: {os.cpu_count()}")
