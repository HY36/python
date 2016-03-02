#_*_ coding:utf-8 _*_
import os

key=input('Please enter what you want to search:\n')

def find_files(path,key):
    abspath=os.path.abspath(path)
    for x in os.listdir(path):
        absfile=os.path.join(path,x)
        if os.path.isfile(absfile):
            if key in os.path.split(x)[1]:
                print(os.path.abspath(absfile))
        if os.path.isdir(absfile):
            find_files(absfile,key)

find_files('.',key)
