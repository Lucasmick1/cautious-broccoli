import random


def create_spaces(palavra):
    spaces = []
    for i in palavra:
        spaces.append("_")
    return spaces


def get_file(fileName):
    file = open(fileName, "r")
    return file


def file_to_array(file):
    array = [word.strip() for word in file]
    file.close()
    return array


def get_secret_word():
    index = random.randrange(0, 5)
    file = get_file('palavras.txt')
    palavras = file_to_array(file)

    return palavras[index]


def jogar():

    secret_word = get_secret_word()
    spaces = create_spaces(secret_word)

    dead = False
    win = False

    while not dead and not win:
        print(" O")
        print("\|/")
        print(" |")
        print("/ \\")
        print(" ".join(spaces))
        print("")
        chute = input("Qual a letra? ").strip().lower()
        i = 0
        for char in secret_word:
            if char == chute:
                spaces[i] = chute

            i = i + 1

        stage = str("".join(spaces))
        if stage == secret_word:
            win = True
            print("""
                  
                  ACERTOU !!! A PALAVRA ERA
                  {}
                  """.format(secret_word))

    return


if __name__ == "__main__":
    jogar()
