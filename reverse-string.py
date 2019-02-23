from pprint import pprint

# Reverse a string in place

# Input: string
# Output: string

# Strings are immutable in python, so use a list

# "hello" > "olleh"

# h e l l o
# 0 1 2 3 4 

# 0 <-> 4
# or.. 0 <-> -1

# 1 <-> 3
# or.. 1 <-> -2
# 2 stays in place (no work done)

# h e l l o o
# 0 1 2 3 4 5
#   ^     ^

# 0 <-> 5
# 1 <-> 4
# 2 <-> 3

# Establish a front and end pointer to track indices to swap

# As long as beginning pointer is less than or equal to end pointer,
# swap the elements in those indices

def rev_string_in_place(str):

    sample_test = 5/2  # Rounds down

    list_string = list(str)
    length = len(str)

    for i in range(0, length/2):
        # len(hello) is 5, length is 2
        # list_string[2 - 1 - i]
        list_string[i], list_string[len(str) - 1 - i] = list_string[len(str) - 1 - i], list_string[i]

    print(sample_test)
    return list_string

print(rev_string_in_place("Hello"))


def rev_str_in_place_pointers(list_chars):

    left_pointer = 0
    right_pointer = len(list_chars) - 1

    # As long as left pointer is less than right pointer..
    # Swap the pointers - middle letter can be left alone if it's an odd # of chars

    while left_pointer < right_pointer:
        list_chars[left_pointer], list_chars[right_pointer] = list_chars[right_pointer], list_chars[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return list_chars


print(rev_str_in_place_pointers(['H', 'E', 'N', 'L', 'O']))

# class Test(object):
#     def __init__(self, a):
#         self.a = a
#     def __repr__(self):
#         return "<Repr Test a:%s>" % (self.a)
#     def __str__(self):
#         return "From str method of Test: a is %s" % (self.a)

# Reverse string using a stack

class Stack(object):

    def __init__(self):
        self.items = []

    def __str__(self):
        return "String of self.items: " + str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Can't remove from empty stack")
            return False
        self.items.pop()
    
    def reverse_order(self, string):
        
        # Create an empty stack, and keep track of the length of the string
        print("String is: ", string)
        length_str = len(string)
        string_stack = Stack() # this is a list, refer to elements using string_stack.items
        
        for i in range(0, length_str, 1):
            print("String at i is: ", string[i])
            string_stack.push(string[i])
        
        # p = pprint(vars(string_stack))

        reversed_string = ""

        for i in range(0, length_str, 1):
            reversed_string += string_stack.items.pop()

        return reversed_string

# H E L L O 
# 1 2 3 4 5 Normal access sequence
# 5 4 3 2 1 Access via Stack
