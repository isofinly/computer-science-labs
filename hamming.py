from ast import Num
from functools import reduce
import operator as op

# import numpy as np
# bits = np.random.randint(0,2,16)

def hamming(bits):
    return(reduce(op.xor, [i for i, bit in enumerate(bits) if bit]))
if __name__ == '__main__':
    try:
        bits = []
        NumInput = input('Enter the numbers in one line without separations: ')
        for i in range(len(NumInput)):
            bits.append(NumInput[i])
        bits = list(map(int, bits))

        # print((bits), type(bits))
        # 1100101011110110
        # 1100101011010110
        # bits = [1,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0]
        
        if hamming(bits) == 0:
            print("Your message was not corrupted. Here it is: ", NumInput)
        if hamming(bits) > 0:
            print("One bit was corrupted. Its position is: ", hamming(bits))
    except ValueError or SyntaxError:
        print('You are doing something wrong :)')