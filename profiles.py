MIN_AGE = 18
CURRENT_YEAR =  2026
players = {
    "Ernie": {
        "naam": "Ernie",
        "geboortedatum": "01-01-1990",
        "gender": "man",
        "aanspreekvorm": "meneer",
        "saldo": 100.00,
        "gespeelde_spellen": {
            "Blackjack": 1
        }
    },
    "Bert": {
        "naam": "Bert",
        "geboortedatum": "20-02-1990",
        "gender": "man",
        "aanspreekvorm": "meneer",
        "saldo": 200.00,
        "gespeelde_spellen": {
            "Fruitmachine": 1
        }
    },
    "Anna": {
        "naam": "Anna",
        "geboortedatum": "14-06-1994",
        "gender": "vrouw",
        "aanspreekvorm": "mevrouw",
        "saldo": 150.00,
        "gespeelde_spellen": {}
    }
}
current_player = None

def determine_salutation(gender):
    if gender == "man":
        aanspreekvorm = "meneer"
    elif gender == "vrouw":
        aanspreekvorm = "mevrouw"
    elif gender == "anders":
        aanspreekvorm = input("Hoe wilt u aangesproken worden?")
    else:
        aanspreekvorm = "heer/mevrouw/anders"
    return aanspreekvorm

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

def initialize_player(total_cost):
    global players
    global current_player

#   players = create_start_players()
    name = input("Wat is je naam?").capitalize()
    current_player = name

    if name in players:
        profile = players[current_player]
        gender = profile["gender"]
        salutation = determine_salutation(gender)
        saldo = profile["saldo"]

        print(f"""
            Beste {salutation} {current_player},
            Wij heten u graag welkom bij Casino de Gouden Driehoek!
            -------------------------------------------------------
            Je huidige saldo is: €{saldo:.2f}
        """)
        return saldo
    else:
        create_account(total_cost, name)
        profile = players[current_player]
        saldo = profile["saldo"]
        start_saldo = saldo + total_cost
        gender = profile["gender"]
        salutation = determine_salutation(gender)

        print(f"""
            Beste {salutation} {current_player},
            Wij heten u graag welkom bij Casino de Gouden Driehoek!
            -------------------------------------------------------
            Startbudget:  €{start_saldo:.2f}
            Vaste kosten: €{total_cost:.2f}
            Saldo:        €{saldo:.2f}
        """)
        return saldo

def create_account(total_cost, name=None):
    global current_player
    if name is None:
        name = input("Wat is je naam?").strip().capitalize()
    if name in players:
        print(f"Dit account: {name} bestaat al")
        return
    print(f"Nieuw account wordt aangemaakt voor: {name}")
    leeftijd, geboortedatum = leeftijdscheck()
    gender = input("Bent u een man, vrouw of anders").strip().lower()
    salutation = determine_salutation(gender)
    while True:
        start_budget = float(input("Met welk budget wilt u beginnen?").replace(",", "."))
        if start_budget >= total_cost:
            print("U heeft genoeg geld voor toegang tot het casino, veel speelplezier!")
            break
        print(f"""U heeft helaas niet genoeg geld voor toegang. 
        Er moet minimaal €{total_cost:.2f} beschikbaar zijn""")
    saldo = start_budget - total_cost
    print(f"Startbudget: €{start_budget:.2f}")
    print(f"Vaste kosten: €{total_cost:.2f}")
    print(f"Saldo: €{saldo:.2f}")
    profiel = {
        "naam": name,
        "geboortedatum": geboortedatum,
        "gender": gender,
        "aanspreekvorm": salutation,
        "saldo": saldo,
        "gespeelde_spellen": {}
    }
    current_player = name
    players[name] = profiel

def update_current_balance(saldo):
    players[current_player]["saldo"] = saldo

def get_current_balance():
    return players[current_player]["saldo"]

def show_account():
    profile = players[current_player]
    print(profile)

def show_all_players():
    for name, profile in players.items():
        print(f"- {name}: saldo €{profile['saldo']:.2f}")

def switch_account():
    global current_player

    name = input("Naar welk account wilt u wisselen? ").strip().capitalize()

    if name not in players:
        print(f"Het account {name} bestaat niet.")
        return

    current_player = name
    profile = players[current_player]

    print(f"U bent gewisseld naar het account van {current_player}.")
    print(f"Het huidige saldo is €{profile['saldo']:.2f}.")

def remove_account():
    global current_player

    name = input("Welk account wilt u verwijderen? ").strip().capitalize()

    if name not in players:
        print(f"Het account {name} bestaat niet.")
        return

    if len(players) == 1:
        print("Het laatste account mag niet verwijderd worden.")
        return

    del players[name]
    print(f"Het account {name} is verwijderd.")

    if name == current_player:
        current_player = list(players.keys())[0]
        print(f"U bent automatisch gewisseld naar {current_player}.")

def register_played_game(game_name):
    profile = players[current_player]
    played_games = profile["gespeelde_spellen"]

    if game_name in played_games:
        played_games[game_name] += 1
    else:
        played_games[game_name] = 1


