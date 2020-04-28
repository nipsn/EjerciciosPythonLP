import os
def filesize(route):
    print(sum(os.path.getsize(f) for f in os.listdir(route) if os.path.isfile(f)))
filesize(".")