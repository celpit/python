import random

def createlist(number):
    numberlist = []
    
    for i in range(number):
        numberlist.append(random.randrange(1, 100, 1))
    
    #print(numberlist)
    return numberlist


def listsort(numberlist):
    sortedlist = []
    numberlistsize = len(numberlist)

    for i in range(numberlistsize):
        listsize = len(sortedlist)
        inserted = False
        for j in range(listsize):
            if numberlist[i] < sortedlist[j]:
                sortedlist.insert(j, numberlist[i])
                inserted = True
                break
        if inserted == False:
            sortedlist.append(numberlist[i])
            
    return sortedlist    

def testsortedlist(numberlist):
    listsize = len(numberlist)
    passed = 'pass'

    for i in range(listsize - 1):
        if numberlist[i] > numberlist[i + 1]:
            passed = 'fail'
            break

    print('Testing list of size ', listsize, '...', passed)

def main():

    number = int(input('Enter Number:'))
    addlist = createlist(number)
    sortlist = listsort(addlist)
    print(sortlist)

    number = 5
    numlist = createlist(number)
    sortedlist = listsort(numlist)
    testsortedlist(sortedlist)

    number = 10
    numlist = createlist(number)
    sortedlist = listsort(numlist)
    testsortedlist(sortedlist)

    number = 25
    numlist = createlist(number)
    sortedlist = listsort(numlist)
    testsortedlist(sortedlist)

    number = 50
    numlist = createlist(number)
    sortedlist = listsort(numlist)
    testsortedlist(sortedlist)

    number = 100
    numlist = createlist(number)
    sortedlist = listsort(numlist)
    testsortedlist(sortedlist)

if __name__ == '__main__':
    main()