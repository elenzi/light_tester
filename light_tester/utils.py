'''
Created on 2 Mar 2018

@author: elenalanigan
'''

import urllib.request



def parseFile(input):

    if input.startswith('http'):
        N, instructions = None, []
        with urllib.request.urlopen(input) as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return

