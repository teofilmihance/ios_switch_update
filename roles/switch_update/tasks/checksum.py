import sys
import os,sys,subprocess,re
import json
   
file_md5 = format(sys.argv[1])
sw_md5 = format(sys.argv[2])

def verify_md5(file_md5, sw_md5):
    verify = re.search(file_md5.strip(), sw_md5)
    if verify:
        result = True
        
    else:
        result = False
        
    return result

   
v_md5 = verify_md5(file_md5, sw_md5)

print json.dumps({
    "result" : v_md5
})


