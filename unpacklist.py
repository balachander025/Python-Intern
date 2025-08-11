def unpack_tuple(tup):
 
    for index, value in enumerate(tup):
        print(f"Element {index}: {value}")

my_tuple = ('apple', 42, 3.14, True)
unpack_tuple(my_tuple)

