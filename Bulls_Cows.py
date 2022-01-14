# By: Michal Kroupa
import random
import time

def generuj_cislo():
    # List Nahodne generovanych cisel
    random_number = []

    # For cyklus pro 4 cifry
    for i in range(4):

        # Aby první číslice nebyla nula
        if i == 0:
            random_cislo = random.randint(1, 9)
            random_number.append(random_cislo)

        # Další číslice, které mohou být nula
        else:
            random_cislo = random.randint(0, 9)

            # Generování nové číslice, pokud je duplicitní
            while random_cislo in random_number:
                random_cislo = random.randint(0, 9)

            #přidání číslice do listu
            random_number.append(random_cislo)

    # Vrátí list čísel
    return random_number

def kontrola_vstupu():

    # Kontrola, zda uživatel zadal validní vstup
    while True:
        duplikat = False
        list_cislo = []
        hadane_cislo = input("Enter a number: ")

        # Pokud nezadá číslo, nebo má číslo moc/málo cifer, program ho upozorní a uživatel zadává znovu
        if hadane_cislo.isdigit() is False or int(hadane_cislo) < 1000 or int(hadane_cislo) > 9999:
            print("Write only numbers between 1000 and 9999")

        # Pokud je vstup validní
        else:

            # Cyklus, který vstup převede do listu, a u toho kontroluje zda uživatel nezadal duplikát
            for i in hadane_cislo:

                if int(i) in list_cislo:
                    duplikat = True

                list_cislo.append(int(i))

            # Pokud byl nalezen duplikát, program uživatele upozorní a musí zadávat znovu
            if duplikat is True:
                print("No duplicates in your number!")

            # Vstup je validní a bez duplikátů
            else:
                return list_cislo




def sklonovani_bullscows(bulls_cows):

    # Fce na kontrolu počtu bulls/cows, a podle toho jejich skloňování
    if bulls_cows[0] == 1 and bulls_cows[1] == 1:
        print(f"Bull: {bulls_cows[0]}, Cow: {bulls_cows[1]}")

    elif bulls_cows[0] > 1 and bulls_cows[1] == 1:
        print(f"Bulls: {bulls_cows[0]}, Cow: {bulls_cows[1]}")

    elif bulls_cows[0] == 1 and bulls_cows[1] > 1:
        print(f"Bull: {bulls_cows[0]}, Cows: {bulls_cows[1]}")

    else:
        print(f"Bulls: {bulls_cows[0]}, Cows: {bulls_cows[1]}")

def zkontroluj_cislo(hadane_cislo, random_number):

    # Kontrola, Zda uživatel trefil číslo, nebo počet bulls/cows
    bulls_cows = [0, 0]

    # Pokud se uživatel trefil, vrací True
    if hadane_cislo == random_number:
        return True

    # Pokud se netrefil
    else:

        # Enumeruje hadane cislo kvuli kontrole indexu
        for index, cislo in enumerate(hadane_cislo):

            # Pokud cislo sedí s číslem na stejném indexu v náhodně generovaném čísle, je to Bull
            if cislo == random_number[index]:
                bulls_cows[0] += 1

            # Pokud nesedí pozice, ale číslo se v náhodně generovaném čísle nachází, je to Cow
            elif cislo in random_number:
                bulls_cows[1] += 1

        # Volá výpis skloňování
        sklonovani_bullscows(bulls_cows)
        # Vrací False, nebylo uhodnuto
        return False

def zapis_score(nick, guess, seconds):

    #Vytvoří a zapíše uživatelský nick, kolikrát hádal a jak dlouho mu to trvalo
    f = open("score.txt", "a")
    f.write(f"{nick}: {guess} guesses in {seconds} seconds\n")
    f.close()

def main():

    #Hlavní fce celého programu, deklarace proměnných a volání fcí
    oddelovac = "-" * 47
    pocatecni_cas = time.time()
    guesses = 1
    game_running = True
    random_number = generuj_cislo()

    # Základní dialog
    print("Hi there!")
    nickname = input("Enter your nickname to save your guesses! ")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")

    # Hlavní cyklus, která určuje zda je dohráno nebo ne
    while game_running:

        print(oddelovac)
        hadane_cislo = kontrola_vstupu()
        print(oddelovac)

        # Pokud se uživatel trefil, hra končí a vypíšou se statistiky a hodnocení jeho výkonu
        if zkontroluj_cislo(hadane_cislo, random_number) is True:
            koncovy_cas = time.time()
            print("Correct, you've guessed the right number")
            print(f"In {guesses} guesses!")

            if guesses <= 5:
                print("That's amazing!")

            elif guesses <=10:
                print("That's average")

            else:
                print("That's not so good")

            celkovy_cas = round(koncovy_cas - pocatecni_cas, 2)
            print(f"And it took you {celkovy_cas} seconds!")
            zapis_score(nickname, guesses, celkovy_cas)
            game_running = False

        # Pokud se netrefil, přidá se mu jeden guess
        else:
            guesses += 1

#Spustí hlavní cyklus hry
main()