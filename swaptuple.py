def swap_tuple(t):
    if len(t) != 2:
        return "Error: Tuple must contain exactly two elements."
    
    a, b = t      
    return (b, a) 

original = (10, 20)
swapped = swap_tuple(original)
print("Original tuple:", original)
print("Swapped tuple:", swapped)

