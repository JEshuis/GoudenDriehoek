import random
from helpers import uitvraag_inzet
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def play_blackjack(saldo):
    gekozen_inzet = uitvraag_inzet(saldo)
    saldo -= gekozen_inzet
    deck = create_deck(SUITS, RANKS)
    random.shuffle(deck)
    speler_hand = []
    dealer_hand = []
    for _ in range(2):
        draw_card(deck, speler_hand)
        draw_card(deck, dealer_hand)
    show_hand("Jouw hand", speler_hand)
    show_hand("Dealer hand", dealer_hand, True)
    speler_score = calculate_hand_value(speler_hand)
    print(f"Waarde van jouw hand: {speler_score}")
    while calculate_hand_value(speler_hand) < 21:
        keuze = input("Wil je hit of stand? ").lower()
        if keuze == "stand":
            break
        if keuze != "hit":
            print("Kies alsjeblieft 'hit' of 'stand'.")
            continue
        getrokken_kaart = draw_card(deck, speler_hand)
        print(f"Je trekt: {getrokken_kaart}")
        show_hand("Jouw hand", speler_hand)
        speler_score = calculate_hand_value(speler_hand)
        print(f"Waarde van jouw hand: {speler_score}")
        if speler_score > 21:
            print("Bust! Je hebt verloren.")
            return saldo
    print("\nDe dealer is aan de beurt.")
    show_hand("Dealer hand", dealer_hand)
    dealer_score = calculate_hand_value(dealer_hand)
    print(f"Waarde van de dealerhand: {dealer_score}")
    while calculate_hand_value(dealer_hand) < 17:
        getrokken_kaart = draw_card(deck, dealer_hand)
        print(f"Dealer trekt: {getrokken_kaart}")
        show_hand("Dealer hand", dealer_hand)
        dealer_score = calculate_hand_value(dealer_hand)
        print(f"Waarde van de dealerhand: {dealer_score}")
    speler_score = calculate_hand_value(speler_hand)
    dealer_score = calculate_hand_value(dealer_hand)
    print(f"Jouw eindscore: {speler_score}")
    print(f"De eindscore van de dealer: {dealer_score}")
    if dealer_score > 21:
        saldo = (gekozen_inzet * 2) + saldo
        print(f"Jij zat dichter bij de 21! je wint €{gekozen_inzet * 2}, je overgebleven saldo is: €{saldo}")
        return saldo
    elif speler_score > dealer_score:
        saldo = (gekozen_inzet * 1.5) + saldo
        print(f"Jij had een hogere score! je wint: €{gekozen_inzet * 1.5}, je overgebleven saldo is: €{saldo}")
        return saldo
    elif speler_score == dealer_score:
        saldo += gekozen_inzet
        print(f"Gelijkspel! Je krijgt je bedrag: €{gekozen_inzet} terug, je overgebleven saldo is: €{saldo}")
        return saldo
    else:
        print(f"Je hebt je inzet: €{gekozen_inzet} verloren. Je overgebleven saldo is: €{saldo}")
        return saldo


def create_deck(suits,ranks):
    return [f"{rank}{suit}" for suit in suits for rank in ranks]

def draw_card(deck, hand):
    kaart = deck.pop()
    hand.append(kaart)
    return kaart

def show_hand(label, hand, hide_card=False):
    visible_cards = hand.copy()
    if hide_card:
        visible_cards[1] = "??"
    print(f"{label}: {' | '.join(visible_cards)}")

def calculate_card_value(card):
    rank = card[:-1]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    total = 0
    aces = 0
    for card in hand:
        total += calculate_card_value(card)
        if card[:-1] == "A":
            aces +=1
    while total > 21 and aces > 0:
        total -=10
        aces-=1
    return total