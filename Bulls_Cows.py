import random

def generuj_cislo():
    # random_number = random.randint(1000, 9999)
    random_number = [2, 0, 1, 7]
    return random_number

def zkontroluj_cislo(hadane_cislo, random_number):
    bulls_cows = [0, 0]
    if hadane_cislo == random_number:
        return True
    else:
        for index, cislo in enumerate(hadane_cislo):
            if int(cislo) == int(random_number[index]):
                bulls_cows[0] += 1
            elif cislo in random_number:
                bulls_cows[1] += 1
        print(f"Bulls: {bulls_cows[0]}, Cows: {bulls_cows[1]}")
        return False

    
def preved_cislo(hadane_cislo):
    list_cislo = []
    for i in str(hadane_cislo):
        list_cislo.append(int(i))
    return list_cislo

def main():
    guesses = 1
    game_running = True
    random_number = generuj_cislo()
    print("Hi there!")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    while game_running:
        print(oddelovac)
        hadane_cislo = int(input("Enter a number: "))
        print(oddelovac)
        hadane_cislo = preved_cislo(hadane_cislo)
        if zkontroluj_cislo(hadane_cislo, random_number) is True:
            print("Correct, you've guessed the right number")
            print(f"In {guesses} guesses!")
            game_running = False
        else:
            guesses += 1
oddelovac = "-" * 47
main()