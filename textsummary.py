


def textsummary(input):
    countedinput = []
    inputlist = list(input)
    inputlistsize = len(inputlist)
    wordcount = 0
    lettercount = 0
    vowelcount = 0
    sentencecount = 0
    for i in range(inputlistsize):
        # word count
        if i == ' ':
            wordcount = wordcount + 1
        # letter count
        if i != ' ':
            lettercount = lettercount + 1
        # vowel count
        if i == 'a':
            vowelcount = vowelcount + 1
        if i == 'e':
            vowelcount = vowelcount + 1
        if i == 'i':
            vowelcount = vowelcount + 1
        if i == 'o':
            vowelcount = vowelcount + 1
        if i == 'u':
            vowelcount = vowelcount + 1
        # sentence count
        if i == '.':
            sentencecount = sentencecount + 1
        if i == '?':
            sentencecount = sentencecount + 1
        if i == '!':
            sentencecount = sentencecount + 1

    #countedinput.append(wordcount[0])
    #countedinput.append(lettercount[1])
    #countedinput.append(vowelcount[2])
    #countedinput.append(sentencecount[3])

    #return countedinput

    print (wordcount)
    print (sentencecount)
    print (lettercount)
    print (vowelcount)

    return wordcount
    return sentencecount
    return lettercount
    return vowelcount



def main():
    str = (input('Enter Text:'))
    text = textsummary(str)
    #print('Words:' countedinput[0])
    #print('Characters:' countedinput[1])
    #print('Vowels:' countedinput[2])
    #print('Sentences:' countedinput[3])

    #print('Words:' wordcount)
    #print('Characters:' lettercount)
    #print('Vowels:' vowelcount)
    #print('Sentences:' sentencecount)

    print (text)

if __name__ == '__main__':
    main()
