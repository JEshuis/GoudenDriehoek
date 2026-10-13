ENTRY_TICKET = 10.00
MANDATORY_DRINK = 3.00
GAMBLE_TAX = 15.00
TOTAL_COST = ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX

print("Goedemiddag en welkom bij Casino de Gouden Driehoek.")
naam_gast = input("Zou u zo vriendelijk willen zijn ons uw naam en achternaam door te geven").title()
geboortedatum = input("Wanneer bent u geboren, voer dit in als volgt: dd-mm-yyy")
geslacht = input("Bent u een man, vrouw of anders").lower()


if geslacht == "man":
    aanspreekvorm = "meneer"
elif geslacht == "vrouw":
    aanspreekvorm = "mevrouw"
elif geslacht == "anders":
    aanspreekvorm = input("Hoe wilt u aangesproken worden?")

# Onderstaand heb ik .replace opgezocht omdat ik zelf ook steeds per ongeluk "," intyp in plaats van "."
start_budget = float(input("Wat is het budget waarmee u vandaag wilt beginnen?").replace(",","."))
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


