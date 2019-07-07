
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

def palindrome(input):
    rev = reverse(input)
   
    if rev == input:
        return True
    else:
        return False







def main():
    str = (input('Enter Word:'))
    rev = reverse(str)
    print(rev)

    ispalindrome = palindrome(str)
    if ispalindrome:
        print('palindrome')
    else:
        print('not palindrome')


if __name__ == '__main__':
    main()
