def uitvraag_inzet(saldo):
    while True:
            gekozen_inzet = int(input("Hoeveel wilt u inzetten? €"))

            if gekozen_inzet <= 0:
                print("Dat is helaas niet mogelijk, je moet minimaal €1 inzetten.")
            elif gekozen_inzet > saldo:
                print(f"Je mag helaas niet meer uitgeven dan je huidige saldo van €{saldo:.2f}.")
            else:
                return gekozen_inzet