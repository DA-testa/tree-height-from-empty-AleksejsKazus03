import sys
import threading
import numpy

def compute_height(n, parents):
    # print(numpy.array([1,2,3]))
    tree = numpy.zeros(n)
    def height(i):
        if tree[i] != 0:
            return tree[i]
        if parents[i] == -1: 
            tree[i] = 1
        else: 
            tree[i] = height(parents[i]) + 1
        return tree[i]

    for i in range(n):
        height(i)
    return int(max(tree))

def main():
    # implement input form keyboard and from files
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    inputtext= input()
    if "I" in inputtext:
        count=int(input())
        elements = list(map(int, input().split()))
        else:
            print("Input error")
        
    elif "F" in inputtext:
        file=input()
        if "a" not in file:
            with open(str("test/"+file), mode="r") as txt:
                count = int(txt.readline())
                elements = list(map(int, txt.readline().split()))
        else:
            print("error")
            
    print(compute_height(count, elements))
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

