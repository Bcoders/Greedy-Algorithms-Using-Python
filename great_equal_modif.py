#python 3
def IsGreaterOrEqual(num, max_num):
    num1 = int(str(num)+str(max_num))
    max_num1 = int(str(max_num)+str(num))
    if(num1 > max_num1):
        return True

    else:
        return False

def main():
    num = map(int, input())
    int_list = ([int(x) for x in input().split()])
    max_num = 0
    greatest_num = ''

    while (int_list):
        index = 0
        max_num = int_list[0]
        while(index < len(int_list)-1):
            if (IsGreaterOrEqual(int_list[index+1], max_num)):
                max_num = int_list[index +1]
            else:
                max_num = max_num
                index = index+1
            
        
        greatest_num += str(max_num)
        int_list.remove(max_num)
        
    print(greatest_num)


main()
                
                
            
        
    
    
    
    
