import card_tests
import playing_cards
def deal_cards():
    deck = playing_cards.build_deck()
    playing_cards.shuffle(deck)
    return deck[0:5]
def main():
    hand = deal_cards()
    print("Hand dealt is : ")
    for card in hand:
        print(card['face'] ,"of" ,card['suit'])
    print("This hand contains:")
    if card_tests.is_straight_flush(hand):
        print("A Straight Flush")
    elif card_tests.is_straight(hand):
        print("A Straight")
    elif card_tests.is_flush(hand):
        print("A Flush")
    elif card_tests.is_full_house(hand):
        print("A Full House")
    elif card_tests.is_4_of_a_kind(hand):
        print("A 4 of a Kind")
    elif card_tests.is_3_of_a_kind(hand):
        print("A 3 of a kind")
    elif card_tests.is_2_pair(hand):
        print("A 2 pair")
    elif card_tests.is_pair(hand):
        print('A pair')
    elif card_tests.is_high_card(hand):
        print("A High Card")
if __name__ == '__main__':
    main()
