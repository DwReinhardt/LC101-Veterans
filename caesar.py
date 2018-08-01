alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

def alphabet_position(letter):
    tmp = letter.lower()
    return(alphabet[tmp])

def rotate_character(char, rot):
    upper_tracker = False
    answer = ""
    if char.isalpha() == False:
        return char
    else:
        rotated_value = alphabet_position(char) + rot # rotate by rot
        if rotated_value > 25:
            rotated_value = rotated_value % 26
            answer = list(alphabet.keys())[list(alphabet.values()).index(rotated_value)]
            if char.isupper():
                answer = answer.upper()
    return answer

def encrypt(text, rot):
    encrypted = []
    i = 0
    while i < len(text):
        tmp = text[i]
        i = i + 1
        middle_step = rotate_character(tmp, rot)
        print(middle_step)
        encrypted.append(middle_step)
        print(encrypted)
        answer = ''.join(encrypted)           # joins the characters
    print(answer)
        #cypher_msg.append(encrypted))


def main():
    encrypt("Hello, World!", 5)

if __name__ == "__main__":
    main()
