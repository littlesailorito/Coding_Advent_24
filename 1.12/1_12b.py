
def find_sum_of_similarities(filename : str):

   
    left: int=[] 
    right: int=[]
    dis: int=[]
   
   
        
    with open(filename, 'r') as file:
    
        for line in file:
            parts = line.strip().split('   ')  
            left.append(int(parts[0]))
            right.append(int(parts[1]))
                
    
    for element_in_left in left:
        if right.count(element_in_left):
            dis.append(element_in_left*right.count(element_in_left))
        
    return sum(dis)
                    

filename = "data_b"  


print(f"Distance is {find_sum_of_similarities(filename)}")
