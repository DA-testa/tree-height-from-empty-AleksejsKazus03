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
    input=input()
    if "I" in input:
        count=int(input())
        elements = list(map(int, input().split()))
    else:
        print("Input error")
        
    elif "F" in input:
    # let user input file name to use, don't allow file names with letter a
        file=input()
        if "a" in input():
            print("Input error")
        else:
             with open(str("test/"+file), mode="r") as file:
                count = int(file.readline())
                elements = list(map(int, file.readline().split()))
    else:
        print("Input error")
    
    # account for github input inprecision
    # call the function and output it's result
    print(compute_height(count, elements))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

