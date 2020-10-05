print("Hallo, we gaan samen wat getallen vergelijken")

refGetal = int(raw_input("Geef een referentie getal: "))

teller = 1
aantal = 7

while teller <= aantal:
    antwoord = int(raw_input("Geef een getal: "))

    if antwoord < refGetal:
        print("\t " + str(antwoord) + " is kleiner dan " + str(refGetal))
    elif antwoord == refGetal:
        print("\t " + str(antwoord) + " is gelijk aan " + str(refGetal))
    elif antwoord > refGetal:
        print("\t " + str(antwoord) + " is groter dan " + str(refGetal))

print("EINDE")
