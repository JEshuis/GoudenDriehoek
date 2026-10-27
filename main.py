from profiles import (
    initialize_player,
    create_account,
    get_current_balance,
    update_current_balance,
    show_account,
    show_all_players,
    switch_account,
    remove_account,
    register_played_game
)
from games.roulette import speel_roulette
from games.fruitmachine import play_fruitmachine
from games.blackjack import play_blackjack
ENTRY_TICKET = 10.00
MANDATORY_DRINK = 3.00
GAMBLE_TAX = 15.00
TOTAL_COST = ENTRY_TICKET + MANDATORY_DRINK + GAMBLE_TAX

print("Goedemiddag en welkom bij Casino de Gouden Driehoek.")

def toon_saldo(saldo):
    print(f"""
    Je huidige saldo bedraagt: €{saldo:.2f}
    """)

def show_account_menu():
    show_account()
    show_account_keuze = int(input(f"""
    U kunt kiezen uit de volgende account opties, selecteer bijv. alleen het nummmer "1" voor optie 1:
    Optie 1: Toon alle accounts
    Optie 2: Nieuw account
    Optie 3: Wissel account
    Optie 4: Verwijder account
    """))
    if show_account_keuze == 1:
        show_all_players()
        return get_current_balance()
    elif show_account_keuze == 2:
        create_account(TOTAL_COST)
        return get_current_balance()
    elif show_account_keuze == 3:
        switch_account()
        return get_current_balance()
    elif show_account_keuze == 4:
        remove_account()
        return get_current_balance()
    else:
        print("Ongeldige keuze.")
        return get_current_balance()

def main():
    saldo = initialize_player(TOTAL_COST)
    print(f"Controle Saldo in main: €{saldo:.2f}")
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
                Optie 3: Blackjack
                Optie 0: Terug
                """))
                if spelkeuze == 1:
                    saldo = play_fruitmachine(saldo)
                    update_current_balance(saldo)
                    register_played_game("Fruitmachine")
                elif spelkeuze == 2:
                    saldo = speel_roulette(saldo)
                    update_current_balance(saldo)
                    register_played_game("Roulette")
                elif spelkeuze == 3:
                    saldo = play_blackjack(saldo)
                    update_current_balance(saldo)
                    register_played_game("Blackjack")
            case 2:
                toon_saldo(saldo)
            case 3:
                saldo = show_account_menu()
            case 0:
                print(f"""
                Bedankt voor het spelen.
                Je resterende saldo is: €{saldo:.2f}
                Wij zien u graag weer bij Casino de Gouden Driehoek!
                """)
                exit(1)

main()








