#!/usr/bin/env python3

import os
import sys
import struct
import logging

#import utils

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('packfs')

def main():
    dirname = sys.argv[1]
    fsname = sys.argv[2]

    files = os.listdir(dirname)
    offset = 4 + len(files)*21
    
    with open(fsname, 'wb') as f:
        f.write(struct.pack("<i", len(files)))
        for currentfilename in files:
            filesize = os.stat(dirname+"\\"+currentfilename).st_size
            f.write(struct.pack("<13sLL", bytes(currentfilename, 'ascii'), offset, filesize))
            offset += filesize
        for currentfilename in files:
            filesize = os.stat(dirname+"\\"+currentfilename).st_size
            with open(dirname+"\\"+currentfilename, 'rb') as f2:
                payload = f2.read(filesize)
                f.write(payload)

    f.close()
    
if __name__ == '__main__':
    main()
