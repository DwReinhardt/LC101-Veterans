from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ""
    i = 0
    while i < len(text):
        tmp = text[i]
        i += 1
        middle_step = rotate_character(tmp, rot)
        encrypted = encrypted + middle_step
    return encrypted

def main():
    #encrypt(input("what message would you like to encrypt?\n"), int(input("how far would you like to rotate it?\n")))
    string = input("what message would you like to encrypt?\n")
    rot = int(input("how far would you like to rotate it?\n"))
    encrypt(string, rot)

if __name__ == "__main__":
    main()
