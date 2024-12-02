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
                    
        

    except FileNotFoundError:
        print("File not found.")
        return None

# Example usage:
filename = "data_a"  # Replace with your file name


print(f"Distance is {find_two_lowest_in_columns(filename)}")
