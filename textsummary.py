


def textsummary(input):
    f = open(input)
    contents = (f.read())
    trimmedinput = contents.strip()  #input.strip
    countedinput = []
    inputlist = list(trimmedinput)
    inputlistsize = len(trimmedinput)
    wordcount = 1
    lettercount = 0
    vowelcount = 0
    sentencecount = 0
    vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    print(trimmedinput)

    for i in range(inputlistsize):
        # cur is current character in list
        cur = inputlist[i]

        # word count
        if cur == ' ' and inputlist[i - 1] != ' ':
            wordcount = wordcount + 1

        # letter count
        if (cur >= 'a' and cur <= 'z') or (cur >= 'A' and cur <= 'Z'):
            lettercount = lettercount + 1

        # vowel count
        if cur in vowelList:
            vowelcount = vowelcount + 1

        # sentence count
        if cur == '.':
            sentencecount = sentencecount + 1
        elif cur == '?':
            sentencecount = sentencecount + 1
        elif cur == '!':
            sentencecount = sentencecount + 1

    countedinput.append(wordcount)
    countedinput.append(lettercount)
    countedinput.append(vowelcount)
    countedinput.append(sentencecount)

    print(countedinput)

    f.close()

    return countedinput



def main():
    str = (input('Enter Text:'))
    countedlist = textsummary(str)
    print('Words:', countedlist[0])
    print('Characters:', countedlist[1])
    print('Vowels:', countedlist[2])
    print('Sentences:', countedlist[3])

if __name__ == '__main__':
    main()
