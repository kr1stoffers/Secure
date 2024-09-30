import numpy as np

def intro():
    print("1: Шифр Цезаря")
    print("2: Шифр Плейфера")
    print("3: Шифр Виженера")
    print("4: Шифр Хилла")
    print("5: Шифр Виженера c автоматическим выбором ключа")
    print("6: Шифр 'Лесенка'")
    print("7: Шифр вертикальной перестановки")
    return int(input())
    
def shiza(name, shift):
    return "".join(list(map(lambda char: chr((((ord(char) - ord('а') + shift) % 32) + ord('а')) if ((ord(char) + shift) > ord('я')) else (ord(char) + shift)), name )))

def fair():
    
    key = "назммиев"
    
    d = list(key)
    
    matrix = np.zeros((5, 6))
    
    alphabet = [chr(char) for char in range(ord('а'), ord('я') + 1)]

    # print(alphabet)    

    
    
    d.extend(alphabet)   
    # arr
    print(d)    

    # string = "одиннадцать"
    
    
    
# на зм ие вв ад им
# ва ди мд ан ил ов ич
match intro():
    case 1:
        # name = input("Name: ").lower().strip(" ")
        # shift = int(input("Сдвиг: "))
        
        # print(shiza(name, shift))
        
        name = "gkdjf kd d"
        
        # print(name.replace())
    case 2:
        # fair()
        # arr = [["f", "a", "d", "t"], ["g"]]
        print(fair())
    
        
    case 3:
        #end + start - 1 
        True
    case _:
        print("?")