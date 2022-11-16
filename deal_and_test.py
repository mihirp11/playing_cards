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
    if type(card_tests.is_straight_flush(hand)) == int:
        print("A Straight Flush")
    elif type(card_tests.is_straight(hand)) == int:
        print("A Straight")
    elif type(card_tests.is_flush(hand)) == int:
        print("A Flush")
    elif type(card_tests.is_full_house(hand)) == int:
        print("A Full House")
    elif type(card_tests.is_4_of_a_kind(hand)) ==int:
        print("A 4 of a Kind")
    elif type(card_tests.is_3_of_a_kind(hand)) == int:
        print("A 3 of a kind")
    elif type(card_tests.is_2_pair(hand)) == int:
        print("A 2 pair")
    elif type(card_tests.is_pair(hand)) == int:
        print('A pair')
    elif type(card_tests.is_high_card(hand)) == int:
        print("A High Card")
if __name__ == '__main__':
    main()
