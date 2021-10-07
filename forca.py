import random

def get_file(fileName):
    file = open(fileName, "r")
    return file

def get_secret_word():
    index = random.randrange(0, 5)
    file = get_file('palavras.txt')
    palavras = file_to_array(file)
    return palavras[index]

def create_spaces(palavra):
    return ["_" for i in palavra]

def file_to_array(file):
    array = [word.strip() for word in file]
    file.close()
    return array

def input_attempt():
    return input("Qual a letra? ").strip().lower()

def print_char(spaces):
    print(" O")
    print("\|/")
    print(" |")
    print("/ \\")
    print(" ".join(spaces))
    print("")

def print_you_won(secret_word):
    print("""
     Você acertou !!! 
     A palavra era: {}
     """.format(secret_word))

def print_you_lose(secret_word):
    print("""
        Poxa, você perdeu :(
        A palavra era: {}
        """.format(secret_word))

def check_if_won(spaces, secret_word):
    secret_word_join = str("".join(spaces))
    if secret_word_join == secret_word:
        return True
    return False

def fill_spaces(secret_word, emptySpaces, attempt):
    i = 0
    spaces = emptySpaces
    for char in secret_word:
        if char == attempt:
            spaces[i] = attempt
        i += 1
    return spaces

def has_attempts(attempts):
    if attempts > 0:
        return True
    return False

def jogar():

    secret_word = get_secret_word()
    spaces = create_spaces(secret_word)

    dead = False
    win = False
    attempts = len(secret_word)
   
    while not dead and not win:
        attempts -= 1
        
        print_char(spaces)

        attempt = input_attempt()
        spaces = fill_spaces(secret_word, spaces, attempt)

        if check_if_won(spaces, secret_word):
            win = True
            print_you_won(secret_word)
            
        if not has_attempts(attempts):
            dead = True
            print_you_lose(secret_word)
    
    return


if __name__ == "__main__":
    jogar()
