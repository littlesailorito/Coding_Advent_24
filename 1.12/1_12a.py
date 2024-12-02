
def find_two_lowest_in_columns(filename):
    
   
    left=[]
    right=[]
    dis=[]
   
  
        
    with open(filename, 'r') as file:
    
        for line in file:
            parts = line.strip().split('   ')  # Split the line by tabs
            left.append(int(parts[0]))
            right.append(int(parts[1]))
                
    while len(dis)<1000:
        if min(left)<min(right):
            dis.append(min(right)-min(left))
            left.pop(left.index(min(left)))
            right.pop(right.index(min(right)))
        else:
            dis.append(min(left)-min(right))
            left.pop(left.index(min(left)))
            right.pop(right.index(min(right)))
        
    return sum(dis)
                    
        



filename = "data_a"


print(f"Distance is {find_two_lowest_in_columns(filename)}")
