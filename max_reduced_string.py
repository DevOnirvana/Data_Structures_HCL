#Python program to remove duplicates and get the MaxReducedString
def MaxReducedString(s: str):
    # We use a stack for storing characters and append characters to it if they are not repeated
    stack = []
    for char in s:
        # We pop the last element from the stack if it matches the adjacent character
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Append character to the stack since it is different from adjacent character
            stack.append(char)
    
    print(''.join(stack))
    return ''.join(stack)
MaxReducedString('aaabccddd') #Expected output is : abd

        