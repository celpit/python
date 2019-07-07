
def reverse(input):
    inputlist = list(input)
    reverselist = []
    size = len(input)
    index = size - 1
    reversestring = ''

    while index != -1:
        reversestring = reversestring + inputlist[index]
        index -= 1

    return reversestring

def main():
    str = (input('Enter Sentence:'))
    rev = reverse(str)
    print(rev)

if __name__ == '__main__':
    main()
