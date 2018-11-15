# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def binaryGap(N):
    # write your code in Python 3.6
    max_gap = 0
    cur_gap = 0
    got_1 = False
    for i in range(int(math.log(N,2)+1)):
        if (N & (1<<i)) != 0:
            if (cur_gap > max_gap):
                max_gap = cur_gap
            cur_gap = 0
            got_1 = True
        elif (N & (1<<i)) == 0 and got_1:
            cur_gap = cur_gap+1
        elif (N & (1<<i)) == 0 and got_1 == False:
            cur_gap = 0
    
    if(cur_gap > max_gap):
        return cur_gap
    else:
        return(max_gap)


def rotateArray(A, K):
    # write your code in Python 3.6
    if K == 0 or len(A) < 2 or (K == len(A)) or (K % len(A) == 0):
        return A
    elif K > len(A):
        moves = K%len(A)
    else:
        moves = K
    B = []
    LEN = len(A)
    print(moves)
    print(LEN)
    for i in range(moves,LEN):
        B.append(A[i])        
    for i in range(moves):
        B.append(A[i])
    return(B)

def oddOccurInArray(A):
    A.sort()
    count = 1
    i=0
    print(A)
    while i < len(A):
        if i == len(A)-1:
            return(A[i])
        j = i+1     
        while A[i] == A[j]:
            print(i,j,A[i],A[j],count)
            j = j+1
            count = count+1
            if j >= len(A):
                print("Reached here")
                break
        #print(i,j,A[i],A[j],count)
        if count%2 != 0 :
            print("Here")
            return A[i]
        else:
            count = 1
        i = j
    
def shortest_path_of_trailing(A):
    num_of_2 = 0
    num_of_5 = 0
    move_array = []
    for i in range(len(A)):
        for j in range(i):
            pass
            
if __name__ == "__main__":
    print(oddOccurInArray([3,3,3,3,4,4,4,4,5,6,6,6,6,6,6,3,12,4231,4231,12,3,5]))