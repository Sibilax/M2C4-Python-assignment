# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list = [1,2,3]
my_tuple = (1,2,3)
my_float = 10.40
my_integer = 2
my_dictionary = {
    "a key" : "a value"
}

from decimal import Decimal
my_decimal = Decimal(10.40)

# Exercise 2: Round your float up.
import math 
print(math.ceil(my_float))
 
# Exercise 3: Get the square root of your float.
import math 
print(math.sqrt(my_float))

# Exercise 4: Select the first element from your dictionary.
print(my_dictionary["a key"])

# Exercise 5: Select the second element from your tuple.
print(my_tuple[1])

# Exercise 6: Add an element to the end of your list.
my_list.append(4)

# Exercise 7: Replace the first element in your list.
my_list[0] = 5

# Exercise 8: Sort your list alphabetically.
my_list.sort()

# Exercise 9: Use reassignment to add an element to your tuple.

print(id(my_tuple))
my_tuple = my_tuple + (4,)  #respuesta original
print(my_tuple)
print(id(my_tuple))

my_tuple = list(my_tuple) #no sé si esta es la corrección que se me ha pedido
my_tuple.append(5)
print(my_tuple)
my_tuple = list(my_tuple)
print(my_tuple)