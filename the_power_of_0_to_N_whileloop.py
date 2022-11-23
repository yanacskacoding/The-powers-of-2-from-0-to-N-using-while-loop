'''Instructions:
Write a program that asks a user to enter a number and print out the sum of the powers of 2 from 0 to N using while loop.

SUM = 20 + 21+22+...+2N

Example:
>>>
4
The sum is 31.
>>>
2
The sum is 7.
'''

#Code:
# Function which removes any special characters
def remove_special_chars(thisString):
    return (''.join(e for e in thisString if e.isalnum()))

# Function to check if input is a number
def check_int(num): 
    # Statement - if variable is number
    if num.isdigit(): 
        # If the varible is a number, return the value in integer format
        return int(num)
    else:
        # If varible is NOT a number, return error
        print("Input is not a number!")
        # Stopping the code
        exit(1)

# Get input from user
num = input()
# Removing special characters from varible
num = remove_special_chars(num)
# Check if varible is integer
num = check_int(num)

# Defining "result" and "thisNum" so we can use them inside the "while" loop
result = 0
thisNum = 0

# While "thisNum" is NOT equal "num" plus 1 
#( This is needed to run the code the right amount of times)
while thisNum != int(num)+1:
    result = result + (2**thisNum)
    thisNum += 1

print('The sum is', result)