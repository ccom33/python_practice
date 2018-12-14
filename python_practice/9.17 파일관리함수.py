import shutil
shutil.copy("live.txt", "live2.txt")

import os

files = os.listdir("c:\\Program Files")
for f in files:
    print(f)

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)

dumpdir("C:\Program Files (x86)\Adobe")
