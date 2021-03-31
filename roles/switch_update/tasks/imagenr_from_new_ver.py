import sys
import os,sys,subprocess,re
import json

txt = format(sys.argv[1])
x = re.search(r"\b[.].........", txt)
temp = x.group()

a = temp[-1]
if a == '.':
     string = temp[1:-1]
     print(string)
else:
     string = temp[1:]
     print(string)
     
pydict = {"outstring": "string"}