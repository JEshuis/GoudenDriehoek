from games.roulette import uitvraag_inzet

def determine_rolls(round_number):
    resultaat = round_number % 5
    if resultaat == 0:
        return "kers", "citroen", "ster"
    elif resultaat == 1:
        return "kers", "kers", "kers"
    elif resultaat == 2:
        return "ster", "ster", "citroen"
    elif resultaat == 3:
        return "citroen", "kers", "ster"
    elif resultaat == 4:
        return "ster", "ster", "ster"

def determine_payout(rol1, rol2, rol3, inzet):
    if rol1 == rol2 == rol3:
        return inzet * 3
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return inzet
    else:
        return 0


def play_fruitmachine(saldo):
    round_number = 1
    while True:
        print(f"""
        Welkom bij de fruitmachines!
        Je huidige saldo bedraagt {saldo:.2f}
        """)
        start_game = int(input("""
        Wil je beginnen met spelen bij de fruitmachines?
        Optie 1: Ja
        Optie 2: Nee
        """))
        if start_game == 1:
            inzet = uitvraag_inzet(saldo)
            rol1, rol2, rol3 = determine_rolls(round_number)
            print(f"{rol1} | {rol2} | {rol3}")

            payout = determine_payout(
                rol1,
                rol2,
                rol3,
                inzet
            )

            saldo -= inzet
            saldo += payout
            round_number += 1

        elif start_game == 2:
            print(f"""
            Dit is je huidige balans:   {saldo:.2f}
            Je kan in het hoofdmenu een ander spel selecteren of het casino verlaten
            """)
            return saldo