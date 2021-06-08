import sys

def collatz(number):
    if(number % 2 == 0):            #even
        return number // 2
    elif(number % 2 == 1):          #odd
        return 3 * number + 1
    else:
        sys.exit()

print('Enter an integer:')
number = int(input())         #same variable to be passed to function. 
      
print('Collatz Sequence')   
print(number)

while number != 1:
    number = collatz(number)
    print(number)