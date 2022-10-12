from functools import reduce
import operator as op

def fun_1():
    bits = []
    NewNumInput = []
    NumInput = input('Enter the numbers in one line without separations: ')
    for i in range(len(NumInput)):
        bits.append(NumInput[i])
        bits = list(map(int, bits))
    if hamming(bits) == 0:
        print("Your message was not corrupted. Here it is: ", NumInput)
    if hamming(bits) > 0:
        print("One bit was corrupted. Its position is: ", hamming(bits))
        if (NumInput[hamming(bits)-1]) == 0:
            NewNumInput = list(NumInput)
            NewNumInput[hamming(bits)-1] = '0'
            NewNumStr = ''.join(NewNumInput)
            print('Corrected code: ', NewNumStr)
        else:
            NumInput[hamming(bits)-1].replace('0','1',1)
            NewNumInput = list(NumInput)
            NewNumInput[hamming(bits)-1] = '1'
            NewNumStr = ''.join(NewNumInput) 
            print('Corrected code a: ',NewNumStr)


def hamming(bits):
    return(reduce(op.xor, [i for i, bit in enumerate(bits) if bit]))

if __name__ == '__main__':
    try:
        fun_1()
    except ValueError or SyntaxError:
        print('You are doing something wrong :)')