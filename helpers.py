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
