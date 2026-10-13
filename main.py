from games.roulette import speel_roulette
from games.fruitmachine import play_fruitmachine
ENTRY_TICKET = 10.00
MANDATORY_DRINK = 3.00
GAMBLE_TAX = 15.00
TOTAL_COST = ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX
MIN_AGE = 18
CURRENT_YEAR =  2026

print("Goedemiddag en welkom bij Casino de Gouden Driehoek.")
def determine_salutation():
    naam_gast = input("Zou u zo vriendelijk willen zijn ons uw naam en achternaam door te geven").title()
    geslacht = input("Bent u een man, vrouw of anders").strip().lower()
    if geslacht == "man":
        aanspreekvorm = "meneer"
    elif geslacht == "vrouw":
        aanspreekvorm = "mevrouw"
    elif geslacht == "anders":
        aanspreekvorm = input("Hoe wilt u aangesproken worden?")
    else:
        aanspreekvorm = "heer/mevrouw/anders"
    return naam_gast, aanspreekvorm

def bereken_leeftijd(geboortedatum):
    birth_day, birth_month, birth_year = map(int, geboortedatum.split("-"))
    return CURRENT_YEAR - birth_year

def leeftijdscheck():
    geboortedatum = input("Wanneer bent u geboren, voer dit in als volgt: dd-mm-yyy")
    leeftijd = bereken_leeftijd(geboortedatum)
    if leeftijd < MIN_AGE:
        print("Je bent helaas niet oud genoeg voor Casino de Gouden Driehoek")
        exit(1)
    return leeftijd, geboortedatum

def inleg_berekenen():
    # Onderstaand heb ik .replace opgezocht omdat ik zelf ook steeds per ongeluk "," intyp in plaats van "."
    start_budget = float(input("Wat is het budget waarmee u vandaag wilt beginnen?").replace(",", "."))
    saldo = start_budget - TOTAL_COST
    if start_budget > (ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX):
        toelatingseis = "U heeft genoeg geld voor toegang tot het casino, veel speelplezier!"
    else:
        toelatingseis = "U heeft helaas niet genoeg geld voor toegang en zult uw saldo moeten opwaarderen"
    return start_budget, saldo, toelatingseis

def show_welcome_message(
        naam_gast,
        aanspreekvorm,
        start_budget,
        saldo,
        toelatingseis
        ):
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

def toon_saldo(saldo):
    print(f"""
    Je huidige saldo bedraagt: €{saldo:.2f}
    """)

def toon_account(
        naam_gast,
        aanspreekvorm,
        leeftijd,
        geboortedatum,
    ):
    print(f"""
    Wij hebben de onderstaande gegevens van u bij ons geregistreerd staan:
    naam:           {naam_gast}
    aanspreekvorm:  {aanspreekvorm}
    leeftijd:       {leeftijd}
    geboortedatum:  {geboortedatum}
    """)

def main():
    naam_gast, aanspreekvorm = determine_salutation()
    leeftijd, geboortedatum = leeftijdscheck()
    start_budget, saldo, toelatingseis = inleg_berekenen()
    show_welcome_message(
        naam_gast,
        aanspreekvorm,
        start_budget,
        saldo,
        toelatingseis
    )
    while True:
        hoofdmenu = int(input("""
        Selecteer uit een van de opties wat u vandaag wilt doen:
        Optie 1: Spellen
        Optie 2: Saldo
        Optie 3: Account
        Optio 0: Stop
        """))

        if not isinstance(hoofdmenu, int):
            hoofdmenu = int(input("Geef alsjeblieft je keuze aan door bijvoorbeeld alleen een 1 te typen voor optie 1"))

        match hoofdmenu:
            case 1:
                spelkeuze = int(input("""
                Je hebt de keuze uit de volgende spellen:
                Optie 1: Fruitmachine
                Optie 2: Roulette
                Optie 0: Terug
                """))
                if spelkeuze == 1:
                    saldo = play_fruitmachine(saldo)
                elif spelkeuze == 2:
                    saldo = speel_roulette(saldo)
            case 2:
                toon_saldo(saldo)
            case 3:
                toon_account(
                    naam_gast,
                    aanspreekvorm,
                    leeftijd,
                    geboortedatum
                )
            case 0:
                print(f"""
                Bedankt voor het spelen {aanspreekvorm} {naam_gast}.
                Je resterende saldo is: {saldo:.2f}
                Wij zien u graag weer bij Casino de Gouden Driehoek!
                """)
                exit(1)

main()








