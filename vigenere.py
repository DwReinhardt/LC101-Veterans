alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_upper = ["A", "B", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def alphabet_position(letter):
    tmp = letter.lower()
    return(alphabet_lower.index(tmp))
    
def rotated_char(index, case):
    if case == "lower":
        return(alphabet_lower[index])
    else:
        return(alphabet_upper[index])


def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    case = "lower"
    if char.isupper() == True:
        case = "upper"
    rotated_value = alphabet_position(char) + rot # rotate by rot
    if rotated_value > 25:
        rotated_value = rotated_value % 26
    answer = rotated_char(rotated_value, case)
    return answer

def encrypt(text, key):
    encrypted = ""
    i = 0
    key_index = 0
    while i < len(text):
        tmp = text[i]
        if text[i].isalpha() == False:
            middle_step = text[i]
        else:
            key_shift = key[key_index]
            key_rotate = alphabet_position(key_shift)#pass key char out to be rotated
            key_index += 1

            middle_step = rotate_character(tmp, key_rotate)
            if key_index == len(key):
                key_index = 0 
        i += 1
        encrypted = encrypted + middle_step
    return print("your encrypted message is: ", encrypted)

def main():
    #encrypt(input("what message would you like to encrypt?\n"), input("What is your key word?\n"))
    encrypt("Hello, World!", "crap")

if __name__ == "__main__":
    main()
