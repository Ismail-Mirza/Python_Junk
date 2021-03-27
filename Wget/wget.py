import urllib.request
import sys

def get_filename(url):
    return url.split("/")[-1]

if len(sys.argv) != 2:
    print("usage:   wget filename")
else:
    url =sys.argv[1]
    filname = get_filename(url)
    with urllib.request.urlopen(url) as data:
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
                print("Downloading.....   %.2f percent "%percent,end='\r', flush=True)
            fh.close()
