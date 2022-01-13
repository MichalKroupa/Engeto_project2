import random

def generuj_cislo():
    random_number = []
    random_cislo = 0
    for i in range(4):

        if i == 0:
            random_cislo = random.randint(1, 9)
            random_number.append(random_cislo)

        else:
            random_cislo = random.randint(0, 9)

            while random_cislo in random_number:
                random_cislo = random.randint(0, 9)

            random_number.append(random_cislo)

    print(random_number)
    return random_number

def kontrola_vstupu():
    while True:
        hadane_cislo = int(input("Enter a number: "))
        if hadane_cislo < 1000 or hadane_cislo > 9999:
            print("Write only numbers between 1000 and 9999")
        else:
            return hadane_cislo



def sklonovani_bullscows(bulls_cows):

    if bulls_cows[0] == 1 and bulls_cows[1] == 1:
        print(f"Bull: {bulls_cows[0]}, Cow: {bulls_cows[1]}")

    elif bulls_cows[0] > 1 and bulls_cows[1] == 1:
        print(f"Bulls: {bulls_cows[0]}, Cow: {bulls_cows[1]}")

    elif bulls_cows[0] == 1 and bulls_cows[1] > 1:
        print(f"Bull: {bulls_cows[0]}, Cows: {bulls_cows[1]}")

    else:
        print(f"Bulls: {bulls_cows[0]}, Cows: {bulls_cows[1]}")

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
        sklonovani_bullscows(bulls_cows)
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
        hadane_cislo = kontrola_vstupu()
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
#  dodelat kontrolu vstupu, aby nebyly duplikaty, cas a score nak