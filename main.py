def caso(fatodef):
    password = ""
    if fatodef == 0:
        password += (random.choice(letters))
        return password
    elif fatodef == 1:
        password += (random.choice(numbers))
        return password
    elif fatodef == 2:
        password += (random.choice(symbols))
        return password
def scelta2():
     while True:
        try:
            scelta = int(input("Di quanti caratteri vuoi generare la password?\n"))
            return scelta
        except:
            print("Devi inserire un numero")
def scelta1():
    while True:
        try:
            scelta1 = int(input("1 per custom 2 per caso\n"))
            if scelta1 == 1 or scelta1 == 2:
                return scelta1
            else:
                print("Il numero selezionato non e corretto")
        except:
            print("Devi inserire un numero")
def main():
    scelta = scelta1()
    password = ""
    if scelta == 1:
        try:
            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            nr_numbers = int(input(f"How many numbers would you like?\n"))
        except:
            print("I numeri inseriti non sembrano corretti")
    if scelta == 1:
        fato1, fato2, fato3 = 0, 0, 0
        while True:
            fatofinal = fato1 + fato2 + fato3
            fato = random.randrange(0, 3)
            numfinal = nr_letters + nr_symbols + nr_numbers
            if fatofinal >= numfinal:
                break
            elif fato == 0 and fato1 < nr_letters and nr_letters > 0:
                password += caso(0)
                fato1 += 1
            elif fato == 1 and fato2 < nr_numbers and nr_numbers > 0:
                password += caso(1)
                fato2 += 1
            elif fato == 2 and fato3 < nr_symbols and nr_symbols > 0:
                password += caso(2)
                fato3 += 1

    if scelta == 2:

        caratteri = scelta2()
        conta = 0
        while conta < caratteri:
            fato = random.randrange(0, 3)
            if fato == 0:
                password += caso(fato)
            elif fato == 1:
                password += caso(fato)
            elif fato == 2:
                password += caso(fato)
            conta += 1
    print(f"la tua password: {password}")
if __name__ == '__main__':
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "_", "-", "[", "]", "{" , "}"]
    main()
    while True:
        choice1 = input("Vuoi genenrare una nuova password? Y N\n").lower()
        if choice1 == "y":
            main()
        elif choice1 == "n":
            print("Grazie di aver utilizzato il password generator")
            break
        else:
            print("Il valore scelto non sembra corretto")
