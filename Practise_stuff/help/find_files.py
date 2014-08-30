import os
import inspect
def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for file in files:
            yield os.path.join(root, file)
            
#print list(recursive_file_gen('C:\Users\oo\Documents\workspace-sts-2.8.1.RELEASE\prectice\object'))
print list(recursive_file_gen('C:\Users\oo\Documents'))

