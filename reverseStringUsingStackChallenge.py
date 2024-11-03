# You will need this class for your solution. Do not edit it.
import stack


# Complete the function definition for reverse_string.
# Use print("messages...") to debug your solution.

def reverse_string(my_string):
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type,
    # and build the solution by filling the bucket within a loop.
    reversed_string = ""
    # Create a new stack
    s = stack.Stack()
    # Iterate through my_string and push the characters onto the stack
    for i in my_string:
        s.push(i)

    # Use a while loop with the exit condition that the stack is empty.
    while not s.is_empty():
        # Within this loop, update reversed_string with characters popped off the stack.
        reversed_string += s.pop()

    # Return the result
    return reversed_string


# debugging
if __name__ == "__main__":
    reversed_string = reverse_string("hello")
    print(reversed_string)
