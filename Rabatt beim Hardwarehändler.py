def calculate_prices(anzahl, preis, kategorie):
    rabattKategorie = {
        "A": 0.1,
        "B": 0.12,
        "C": 0.15,
        "D": 0.2,
        "E": 0.3,
        "andere": 0
    }

    preis = anzahl * preis

    rabatt = preis * rabattKategorie[kategorie]

    netto = preis - rabatt

    mehrwertStr = netto * 0.19

    brutto = netto + mehrwertStr

    return f"{preis}, {rabattKategorie[kategorie]*100}, {rabatt}, {netto}, {mehrwertStr}, {brutto}"

anzahlMause = int(input(">Anzahl der Mäuse: "))
preisJeMaus = float(input(">Preis je Maus: "))
kategorie = input(">Wählen Sie die Kategorie: ")

results = calculate_prices(anzahlMause, preisJeMaus, kategorie)

results = results.split(", ")

print(f"Warenwert ohne Rabatt: {results[0]}")
print(f"Rabatt: {results[1]}")
print(f"Nettobetrag: {results[2]}")
print(f"Mehrwertsteuerbetrag: {results[3]}")
print(f"Bruttobetrag: {results[4]}")