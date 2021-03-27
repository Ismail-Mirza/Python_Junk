import urllib.request
import sys
import time
import termcolor
import colorama

import os
colorama.init()
def get_filename(url):
    return url.split("/")[-1]

if len(sys.argv) != 2:
    print("usage:   wget filename")
else:
    url =sys.argv[1]
    filname = get_filename(url)
    data = None
    start = time.time()
    try:
        while data==None or data.length == None:
            print("[+] Conecting with server.... ",end="\r",flush=True)
            data=urllib.request.urlopen(url)
            end = time.time()
            if end-start >20:
                termcolor.cprint("[-] Connection time out 400")
                sys.exit(1)
    except Exception as msg:
        print(msg)
        sys.exit(1)
    termcolor.cprint("[+] Contected with server\n",end="\r",color="green")
    total_length = data.length
    block = 512
    filesize = 0
    with open(filname,"wb") as fh:
        while True:
            buffer = data.read(block)
            # print(buffer)
            if not buffer:
                break
            filesize += len(buffer)
            fh.write(buffer)
            percent = filesize*100/total_length
            termcolor.cprint("Downloading.....   %.2f percent "%percent,end='\r',color="blue", flush=True)
        fh.close()
