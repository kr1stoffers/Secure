def intro():
    print("1: Шифр Цезаря")
    print("2: Шифр Плейфера")
    print("3: Шифр Виженера")
    print("4: Шифр Хилла")
    print("5: Шифр Виженера c автоматическим выбором ключа")
    print("6: Шифр 'Лесенка'")
    print("7: Шифр вертикальной перестановки")
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

    # print(keyAlphabet)
    matrix = []
    matrix = removeDuplicates(keyAlphabet, matrix)

    text = replaceSpecialChar(list(text))

    encrypted = ""

    def getRowChar(index):
        return (
            matrix[index + 1]
            if int((index + 1) / 6) == int(index / 6)
            else matrix[(index + 1) % 6]
        )

    def getColumnChar(index):
        return matrix[index + 6] if index + 6 <= len(matrix) else matrix[index % 6]

    # def

    def gemini(text, encrypted):
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
                encrypted += getRowChar(indexFirstChar) + getRowChar(indexSecondChar)

            elif (indexFirstChar % 6) == (indexSecondChar % 6):
                encrypted += getColumnChar(indexFirstChar) + (
                    getColumnChar(indexSecondChar)
                )

            else:
                rowFirst = int(indexFirstChar / 6)
                rowSecond = int(indexSecondChar / 6)

                supremacy = rowSecond - rowFirst
                step = abs(supremacy) * 6
                if indexFirstChar > indexSecondChar:
                    indexFirstChar -= step
                    indexSecondChar += step
                else:
                    indexFirstChar += step
                    indexSecondChar -= step
                if supremacy:
                    encrypted += matrix[indexSecondChar] + matrix[indexFirstChar]
                else:
                    encrypted += matrix[indexFirstChar] + matrix[indexSecondChar]

        return encrypted

    print(matrix)
    print(gemini(text, encrypted))


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
        # end + start - 1
        True
    case _:
        print("?")
