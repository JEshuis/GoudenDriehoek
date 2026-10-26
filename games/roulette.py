ROUND_NUMBER = 1
SPIN = (ROUND_NUMBER * 7) % 37

def speel_roulette(saldo):
    gekozen_optie, color_spin, odd_even = show_roulette_options()
    gekozen_inzet = uitvraag_inzet(saldo)
    saldo -= gekozen_inzet
    saldo = winst_berekening(
        gekozen_optie,
        color_spin,
        saldo,
        gekozen_inzet
    )
    return saldo

def show_roulette_options(saldo):
    gekozen_optie = int(input(f"""
            Welkom bij de roulettetafel!
            Je huidige saldo bedraagt: {saldo:.2f}
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
            exit(1)
    if SPIN % 2 == 0 and SPIN <= 18:
        color_spin = "zwart"
        odd_even = "even"
    elif SPIN % 2 == 1 and SPIN <= 18:
        color_spin = "rood"
        odd_even = "oneven"
    elif SPIN % 2 == 0 and SPIN > 18:
        color_spin = "rood"
        odd_even = "even"
    elif SPIN % 2 == 1 and SPIN > 18:
        color_spin = "zwart"
        odd_even = "oneven"
    return gekozen_optie, color_spin, odd_even

def uitvraag_inzet(saldo):
    while True:
            gekozen_inzet = int(input("Hoeveel wilt u inzetten? €"))

            if gekozen_inzet <= 0:
                print("Dat is helaas niet mogelijk, je moet minimaal €1 inzetten.")
            elif gekozen_inzet > saldo:
                print(f"Je mag helaas niet meer uitgeven dan je huidige saldo van €{saldo:.2f}.")
            else:
                return gekozen_inzet

def winst_berekening(gekozen_optie, color_spin, saldo, gekozen_inzet):
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
    return saldo
