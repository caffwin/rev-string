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

    sample = 5/2  # Rounds down

    list_string = list(str)
    length = len(str)

    for i in range(0, length/2):
        # len(hello) is 5, length is 2
        # list_string[2 - 1 - i]
        list_string[i], list_string[len(str) - 1 - i] = list_string[len(str) - 1 - i], list_string[i]

    print(sample)
    return list_string

# print(rev_string_in_place("Hello"))


class Test(object):
    def __repr__(self):
       return "This is a repr"
    def __str__(self):
        return "This is the str"

# Reverse string using a stack

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Can't remove from empty stack")
            return False
        self.items.pop()
    
    def reverse_order(self, string):
        
        # Create an empty stack, and keep track of the length of the string
        length_str = len(string)
        string_stack = Stack() # this is a list
        
        for i in range(0, length_str):
            string_stack.push(string[i])
            
        print("String stack: ", string_stack)
        
        # print(string_stack)
        reversed_string = ""

        # for i in range(0, length_str):
        #     reversed_string += string_stack.pop(i)

        print([str(item) for item in reversed_string])



# H E L L O 
# 1 2 3 4 5 Normal access sequence
# 5 4 3 2 1 Access via Stack
