#Python 3
import sys
import numpy as np
def main():
    list1 = []
    list2 = []
    max_val = 0;
    n = int(input())
    
    line = input()
    for num in line.split():
        list1.append(int(num))
        
    line = input()
    for num in line.split():
        list2.append(int(num))
        
    list1.sort()
    list2.sort()

        
    
    for i in range(int(n)):
        max_val += list1[i]*list2[i];

    print (max_val)

main()
       
            
        
        
