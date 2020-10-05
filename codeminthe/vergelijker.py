print("Hallo, we gaan samen wat getallen vergelijken")

refGetal = input("Geef een referentie getal: ")
refGetal = int(refGetal)

teller = 1
aantal = 7

while teller <= aantal:
    antwoord = int(input("Geef een getal: "))

    if antwoord < refGetal:
        print("\t " + str(antwoord) + " is kleiner dan " + str(refGetal))
    elif antwoord == refGetal:
        print("\t " + str(antwoord) + " is gelijk aan " + str(refGetal))
    elif antwoord > refGetal:
        print("\t " + str(antwoord) + " is groter dan " + str(refGetal))
    teller += 1

print("EINDE")
