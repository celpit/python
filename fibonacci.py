

def fibonacci(x):
    l = []
    a = 3
    prev = 1
    prev2 = 1
    l.append(prev)
    l.append(prev2)
    
    while a <= x:
        current = prev + prev2
        l.append(current)
        prev2 = prev
        prev = current
        a += 1

    return l

def main():
    number = int(input('Enter Number:'))
    fib = fibonacci(number)
    print(fib)
    index = 1
    for x in fib:
        print(index, ' : ', x)
        index += 1


if __name__ == '__main__':
    main()
