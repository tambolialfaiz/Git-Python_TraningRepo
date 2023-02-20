f=open("Demo.txt","w")
print(f.readable())
print(f.writable())
f.close()

import os
print(os.path.isfile("Demo.txt"))

