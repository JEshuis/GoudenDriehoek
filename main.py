ENTRY_TICKET = 10.00
MANDATORY_DRINK = 3.00
GAMBLE_TAX = 15.00
TOTAL_COST = ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX
MIN_AGE = 18
CURRENT_YEAR =  2026
ROUND_NUMBER = 1

print("Goedemiddag en welkom bij Casino de Gouden Driehoek.")
naam_gast = input("Zou u zo vriendelijk willen zijn ons uw naam en achternaam door te geven").title()
geboortedatum = input("Wanneer bent u geboren, voer dit in als volgt: dd-mm-yyy")

birth_day, birth_month, birth_year = map(int, geboortedatum.split("-"))

if CURRENT_YEAR - birth_year < MIN_AGE:
    print("Je bent helaas niet oud genoeg voor Casino de Gouden Driehoek")
    exit(1)

geslacht = input("Bent u een man, vrouw of anders").lower()

if geslacht == "man":
    aanspreekvorm = "meneer"
elif geslacht == "vrouw":
    aanspreekvorm = "mevrouw"
elif geslacht == "anders":
    aanspreekvorm = input("Hoe wilt u aangesproken worden?")

# Onderstaand heb ik .replace opgezocht omdat ik zelf ook steeds per ongeluk "," intyp in plaats van "."
start_budget = float(input("Wat is het budget waarmee u vandaag wilt beginnen?").replace(",", "."))
saldo = start_budget - TOTAL_COST
if start_budget > (ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX):
    toelatingseis = "U heeft genoeg geld voor toegang tot het casino, veel speelplezier!"
else:
    toelatingseis = "U heeft helaas niet genoeg geld voor toegang en zult uw saldo moeten opwaarderen"

# Onderstaand heb ik :.2f opgezocht zodat bedragen 2 "00" achter de komma krijgen en echt op bedragen lijken
print(f"""
    Beste {aanspreekvorm.lower()} {naam_gast},
    Wij heten u graag welkom bij Casino de Gouden Driehoek!
    -------------------------------------------------------
    Startbudget:    €{start_budget:.2f}
    Vaste kosten:   €{TOTAL_COST:.2f}
    Saldo:          €{saldo:.2f}

    {toelatingseis}
""")

while True:
    ROUND_NUMBER += 1
    SPIN = (ROUND_NUMBER * 7) % 37
    gekozen_optie = int(input("""
        Welkom bij de roulettetafel!
        Je kan kiezen uit de volgende opties:
        Optie 1: Rood
        Optie 2: Zwart
        Optie 3: Even
        Optie 4: Oneven
        Optie 0: Stop
        """))

    if not isinstance(gekozen_optie, int):
        gekozen_optie = int(input("Geef alsjeblieft je keuze aan door bijvoorbeeld alleen een 1 te typen voor optie 1"))

    # Ik ben hier voor break i.p.v. exit gegaan omdat anders de print niet meer goed uitkomt onderaan de applicatie
    if gekozen_optie == 0:
        break

    while True:
        gekozen_inzet = int(input("Hoeveel wilt u inzetten? €"))

        if gekozen_inzet <= 0:
            print("Dat is helaas niet mogelijk, je moet minimaal €1 inzetten.")
        elif gekozen_inzet > saldo:
            print(f"Je mag helaas niet meer uitgeven dan je huidige saldo van €{saldo:.2f}.")
        else:
            break

    saldo -= gekozen_inzet

    if SPIN % 2 == 0 and SPIN <= 18:
        color_spin = "zwart"
    elif SPIN % 2 == 1 and SPIN <= 18:
        color_spin = "rood"
    elif SPIN % 2 == 0 and SPIN > 18:
        color_spin = "rood"
    elif SPIN % 2 == 1 and SPIN > 18:
        color_spin = "zwart"

    if gekozen_optie == 1 and color_spin == "rood":
        saldo = saldo + (gekozen_inzet * 2)
        print(f"De bal land op {color_spin}, je hebt gewonnen! Je wint: €{gekozen_inzet * 2:.2f}")
    elif gekozen_optie == 2 and color_spin == "zwart":
        saldo = saldo + (gekozen_inzet * 2)
        print(f"De bal land op {color_spin}, je hebt gewonnen! Je wint: €{gekozen_inzet * 2:.2f}")
    elif gekozen_optie == 3 and SPIN % 2 == 0:
        saldo = saldo + (gekozen_inzet * 2)
        print(f"De bal land op een even getal, je hebt gewonnen! Je wint: €{gekozen_inzet * 2:.2f}")
    elif gekozen_optie == 4 and SPIN % 2 == 1:
        saldo = saldo + (gekozen_inzet * 2)
        print(f"De bal land op een oneven getal, je hebt gewonnen! Je wint: €{gekozen_inzet * 2:.2f}")
    else:
        print(f"""
        De bal land op, {SPIN}, dit is {color_spin} jij koos helaas voor optie: {gekozen_optie}
        Je hebt helaas verloren, je saldo bedraagt: €{saldo:.2f}""")

    print(f"Je huidige saldo bedraagt: €{saldo:.2f}")

print(f"""Bedankt voor het spelen bij Casino de Gouden Driehoek
Je huidige saldo bedraagt: {saldo:.2f}.
Wij hopen je snel weer te zien!""")






