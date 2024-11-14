import math


def intro():
    print("1: Шифр Цезаря")
    print("2: Шифр Плейфера")
    print("3: Шифр Виженера")
    print("4: Шифр Хилла")
    print("5: Шифр 'Лесенка'")
    print("6: Шифр вертикальной перестановки")
    return int(input())


def shiza(text, shift):
    return "".join(
        list(
            map(
                lambda char: chr(
                    (((ord(char) - ord("а") + shift) % 32) + ord("а"))
                    if ((ord(char) + shift) > ord("я"))
                    else (ord(char) + shift)
                ),
                text,
            )
        )
    )


def removeDuplicates(arr, result):
    for char in arr:
        if char not in result:
            result.append(char)
    return result


def replaceSpecialChar(arr):
    arr = [{"й": "и", "ё": "е", "ъ": "ь"}.get(char, char) for char in arr]
    return arr


def fair(text, key):
    keyAlphabet = list(key)

    alphabet = [chr(char) for char in range(ord("а"), ord("я") + 1)]

    keyAlphabet.extend(alphabet)
    keyAlphabet = replaceSpecialChar(keyAlphabet)

    matrix = []
    matrix = removeDuplicates(keyAlphabet, matrix)

    text = replaceSpecialChar(list(text))

    def getRowChar(index, de):
        return (
            matrix[index + de]
            if int((index + de) / 6) == int(index / 6)
            else matrix[index - (5 * de)]
        )

    def getColumnChar(index, de):
        return (
            matrix[index + (6 * de)]
            if index + (6 * de) <= len(matrix)
            else matrix[index - (25 * de)]
        )

    def gemini(text, flag=True):
        encrypted = ""

        de = 1 if flag else -1

        if flag:
            for i in range(len(text) - 1):
                if text[i] == text[i + 1]:
                    text.insert(i + 1, "ы")
                    gemini(text)
                    break
            if len(text) % 2 != 0:
                text.append("ы")

        for i in range(0, len(text) - 1, 2):
            indexFirstChar = matrix.index(text[i])
            indexSecondChar = matrix.index(text[i + 1])

            if int(indexFirstChar / 6) == int(indexSecondChar / 6):
                encrypted += getRowChar(indexFirstChar, de) + getRowChar(
                    indexSecondChar, de
                )

            elif (indexFirstChar % 6) == (indexSecondChar % 6):
                encrypted += getColumnChar(indexFirstChar, de) + (
                    getColumnChar(indexSecondChar, de)
                )

            else:
                indexFirstCharColumn = indexFirstChar % 6
                indexSecondCharColumn = indexSecondChar % 6
                diff = abs(indexFirstCharColumn - indexSecondCharColumn)
                if indexFirstCharColumn < indexSecondCharColumn:
                    indexFirstChar += diff
                    indexSecondChar -= diff
                else:
                    indexFirstChar -= diff
                    indexSecondChar += diff

                encrypted += matrix[indexFirstChar] + matrix[indexSecondChar]

        return encrypted

    for i in range(5):
        for j in range(6):
            print(matrix[i * 6 + j], end=" ")
        print()
    res = gemini(text)
    print("Encryption: " + res)
    print("Decryption: " + gemini(res, False))


def vigenere(text, key):
    # end + start - 1
    alphabet = [chr(char) for char in range(ord("а"), ord("я") + 1)]
    alphabet.insert(6, "ё")

    textLength = len(text)
    keyLength = len(key)
    encrypted = ""

    if textLength > keyLength:
        key = (key * (math.ceil(textLength / keyLength)))[:textLength]
    else:
        key = key[:textLength]

    print(text)
    print(key)

    for i in range(textLength):
        indexEncChar = alphabet.index(text[i]) + alphabet.index(key[i])
        encrypted += alphabet[
            (
                (indexEncChar)
                if indexEncChar < len(alphabet)
                else int(indexEncChar % len(alphabet))
            )
        ]
    print("Encryption: " + encrypted)

    decrypted = ""

    for i in range(len(encrypted)):
        decrypted += alphabet[
            abs(alphabet.index(encrypted[i]) - alphabet.index(key[i]))
        ]
    print("Decryption: " + decrypted)


def sHill():

    True


def stairs(text):
    # И Т О И О К Н Т Н И Г Н А Ь В Ч
    #  С Р Ф Л В О С А Т Н Е Н Д Е И

    encrypted = "".join(
        [text[i] for i in range(0, len(text), 2)]
        + [text[i] for i in range(1, len(text), 2)]
    )

    decrypted = ""
    half = math.floor(len(encrypted) / 2)
    leftPart = encrypted[:half]
    rightPart = encrypted[half:]
    print(leftPart)
    print(rightPart)
    for i in range(half - 1):
        decrypted += leftPart[i] + rightPart[i]
    decrypted += rightPart[half - 1]
    print("Encryption: " + encrypted)

    print("Decryption: " + decrypted)


match intro():
    case 1:
        text = input("Текст: ").lower().replace(" ", "")
        shift = int(input("Сдвиг: "))

        print(shiza(text, shift))
    case 2:
        text = input("Текст: ").lower().replace(" ", "")
        key = input("Ключ: ").lower().replace(" ", "")

        fair(text, key)

    case 3:
        text = input("Текст: ").lower().replace(" ", "")
        key = input("Ключ: ").lower().replace(" ", "")
        # print(key * 2)°͡

        vigenere(text, key)
    case 4:
        text = input("Текст: ").lower().replace(" ", "")

    case 5:
        text = input("Текст: ").lower().replace(" ", "")
        stairs(text)
    case _:
        print("?")
