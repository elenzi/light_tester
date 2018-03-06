'''
Created on 2 Mar 2018

@author: elenalanigan
'''
def parseFile(input):

    if input.startswith('http'):
        # use requests
        pass
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return