##Modules --> is a .py file
#import multi
'''import multi as mu ##renaming module name
#print(multi.add(3,6))
print(mu.sub(3,6))

from multi import *
print(add(5,6))
print(sub(5,6))
'''
#module --> A group of functions, variables, calsses(as a file) 
#packages --> group of modules (group of files or dir)
#Library --> group of packages

#library --> collection of books(packages) --> combinations pages(modules)

##OS module
import os
#print(os.environ())
#print(os.getcwd()) # we get current working dir
#print(os.getuid())
#print(os.getgid())
#print(os.getpid())

#print(os.listdir())
for j in (os.walk(r'F:\My_Python_Personal')):
    print(j)
#print(os.chroot('path'))