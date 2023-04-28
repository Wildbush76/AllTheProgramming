import copy


class matrixWord:
    @staticmethod
    def encrypt(string):
        words = []
        for i in range(len(string)):
            words.append(string[i:] + string[:i])
        wordsSorted = sorted(words)
        output = "".join([x[-1] for x in wordsSorted])
        for i, word in enumerate(wordsSorted):
            if word == string:
                return output, i + 1

    @staticmethod
    def doing(theLetters, pos, string):
        while len(theLetters[pos]) < len(string):
            letter = theLetters[pos][-2]
            count = []
            for index, le in enumerate(theLetters):
                if le[-1] == letter and le is not theLetters[pos]:
                    count.append(index)
            if len(count) > 1:
                for i in count:
                    l2 = copy.deepcopy(theLetters)
                    l2[pos].insert(-1, theLetters[i][0])
                    l2[i] = ["", ""]
                    output = matrixWord.doing(l2, pos, string)
                    if output != None:
                        theLetters = output
                        break
                else:
                    return
            elif len(count) == 0:
                return
            else:
                theLetters[pos].insert(-1, theLetters[count[0]][0])
                theLetters[count[0]] = ["", ""]
                print(theLetters[count[0]])
        letter = theLetters[pos][-2]
        for i in theLetters:
            if i[-1] == letter and i != theLetters[pos]:
                if i[0] != theLetters[pos][-1]:
                    return
                else:
                    break
        else:
            return
        e, index = matrixWord.encrypt("".join(theLetters[pos]))
        if e != string or index != pos+1:
            return
        return theLetters

    @staticmethod
    def decrypt(string, pos):
        theLetters = [[x, string[i]]
                      for i, x in enumerate(sorted(list(string)))]
        print(theLetters)
        print("doing")
        return "".join(matrixWord.doing(theLetters, pos-1, string)[pos-1])


if __name__ == "__main__":
    choice = input("(1) decrypt\n(2) encrypt")
    if choice == "1":
        encrypted = input("what is it encrypted :")
        index = input("what is its index")
    else:
