import sys
import threading
import numpy

def compute_height(n, parents):
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
    txt=input()
    if "F" in txt:
        filename=input()
        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as fails:
                count = int(fails.readline())
                elements = list(map(int, fails.readline().split()))
        else:
            print("error")
    elif "I" in txt:
        count=int(input())
        elements = list(map(int, input().split()))
    else:
        print("Input error")
    print(compute_height(count, elements))
   
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
