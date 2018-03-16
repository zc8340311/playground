#! /usr/bin/env python

import subprocess as s
import glob
import os

def detect(input,output):
    filenames = glob.glob(input)
    n = 0
    s.call('mkdir -p log/tmp', shell=True)
    s.call('mkdir -p %s'%output, shell=True)
    
    for filename in filenames:
        print n, len(filenames)
        s.call('date', shell=True)
        s.call('rm -f log/tmp/*', shell=True)
        print filename
        baseFilename =  os.path.basename(filename)
        print baseFilename

        s.call('snort -q -r %s -l ./log/tmp -c ../lib/notInGit/etc/snort_just_detect.conf -U'%filename, shell=True)
        
        s.call('cp log/tmp/snort.csv %s/%s_snort.csv'%(output,baseFilename), shell=True)

        s.call('date', shell=True)
        print '--------------------------'
        n += 1

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Detect attacks.')
    parser.add_argument('-i', '--input',
                        help='Input directory.')
    parser.add_argument('-o', '--output',
                        help='Output directory.')

    args = parser.parse_args()
    detect(args.input, args.output)

