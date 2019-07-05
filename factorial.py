import sys
from datetime import datetime 

def factorial(x):

    c = 1

    while x != 1:
        c = c * x
        x = x - 1

    return (c)
        
def factorial2(x):
    if x == 1:
        return 1

    return x * factorial2(x - 1)

def main():
    number = int(input('Enter Number:'))
    start_time = datetime.now()
    fact = factorial2(number)
    end_time = datetime.now()
    print('factorial of  ' + str(number) + ' is ' + str(fact))
    print(end_time - start_time)

if __name__ == '__main__':
    main()
