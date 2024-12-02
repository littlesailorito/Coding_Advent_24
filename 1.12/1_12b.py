pairs= []
def find_two_lowest_in_columns(filename):
    """
    Find the two lowest numbers in each column of a tab-delimited file.
    
    :param filename: Path to the text file.
    :return: A list of tuples where each tuple contains the two lowest numbers in a column.
    """
   
    left=[]
    right=[]
    dis=[]
   
    try:
        
        with open(filename, 'r') as file:
        
            for line in file:
                parts = line.strip().split('   ')  # Split the line by tabs
                left.append(int(parts[0]))
                right.append(int(parts[1]))
                    
        
        for element_in_left in left:
            if right.count(element_in_left):
                dis.append(element_in_left*right.count(element_in_left))
            
        return sum(dis)
                    
        

    except FileNotFoundError:
        print("File not found.")
        return None

# Example usage:
filename = "data_b"  # Replace with your file name


print(f"Distance is {find_two_lowest_in_columns(filename)}")
