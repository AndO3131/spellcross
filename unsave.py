#!/usr/bin/env python3

import sys
import struct
import logging

import unlz

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('unsave')

def main():
    fsname = sys.argv[1]
    with open(fsname, 'rb') as f:
        lz = unlz.LZFile(f)
        while True:
            chunk = lz.read(16)
            if chunk is None:
                break

            print(chunk)

if __name__ == '__main__':
    main()
