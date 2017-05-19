def sum_of_3_5_multiples(x):
    multiple_sum = 0
    for i in range(0, x):
        if (i % 3 == 0 or i % 5 == 0):
            multiple_sum += i

    return multiple_sum
            
        
    
    

