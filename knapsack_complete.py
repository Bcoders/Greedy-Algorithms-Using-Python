#python 3
def knapsack(list1, Total_weight):
    
    list2 = sorted(list1, key=lambda tup: tup[0], reverse=True)
    
    

    Total_weight = Total_weight
    Total_Value = 0

    i = 0

    while(Total_weight!=0 and i <= len(list2)-1):
        item_weight = list2[i][1]
        item_value_per_weight = list2[i][0]
        
        if  item_weight <= Total_weight:
            
            Total_weight = Total_weight - item_weight
            Total_Value += item_value_per_weight * item_weight
            
            
            i+= 1

        else:
            
            Total_Value += Total_weight * item_value_per_weight
            
            Total_weight = 0
            

    print (Total_Value)

def main():
    Num_item, Total_weight = map(int, input().split())
    list1 = []

    for i in range(Num_item):
        item,value = map(int, input().split())
        list1.append([item/value,value])
        
     
    knapsack(list1, Total_weight)

main()
        

        
            
            
    
