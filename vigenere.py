from helpers import alphabet_position, rotate_character

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
            key_rotate = alphabet_position(key_shift)
            key_index += 1

            middle_step = rotate_character(tmp, key_rotate)
            if key_index == len(key):
                key_index = 0 
        i += 1
        encrypted = encrypted + middle_step
    return encrypted

def main():
    #encrypt(input("what message would you like to encrypt?\n"), input("What is your key word?\n"))
    string = input("what message would you like to encrypt?\n")
    key = input("What is your key word?\n")
    encrypt(string, key)

if __name__ == "__main__":
    main()
