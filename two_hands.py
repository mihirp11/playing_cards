import card_tests
import playing_cards
def test_hand(hand):
    if type(card_tests.is_straight_flush(hand)) == int:
        print("A Straight Flush")
        return card_tests.is_straight_flush(hand)
    elif type(card_tests.is_straight(hand)) == int:
        print("A Straight")
        return card_tests.is_straight(hand)
    elif type(card_tests.is_flush(hand)) == int:
        print("A Flush")
        return card_tests.is_flush(hand)
    elif type(card_tests.is_full_house(hand)) == int:
        print("A Full House")
        return card_tests.is_full_house(hand)
    elif type(card_tests.is_4_of_a_kind(hand)) ==int:
        print("A 4 of a Kind")
        return card_tests.is_4_of_a_kind(hand)
    elif type(card_tests.is_3_of_a_kind(hand)) == int:
        print("A 3 of a kind")
        return card_tests.is_3_of_a_kind(hand)
    elif type(card_tests.is_2_pair(hand)) == int:
        print("A 2 pair")
        return card_tests.is_2_pair(hand)
    elif type(card_tests.is_pair(hand)) == int:
        print('A pair')
        return card_tests.is_pair(hand)
    elif type(card_tests.is_high_card(hand)) == int:
        print("A High Card")
        return card_tests.is_high_card(hand)
def main():
    deck = playing_cards.build_deck()
    playing_cards.shuffle(deck)
    hand1 = []
    hand2 = []
    for i in range(0,10):
       if i % 2 == 0:
           hand1.append(deck[i])
       if i % 2 == 1:
           hand2.append(deck[i])
    print("Hand 1 dealt is : ")
    for card in hand1:
        print(card['face'], "of", card['suit'])
    print("This hand contains:")
    result_hand1 = test_hand(hand1)
    print("Hand 2 dealt is : ")
    for card in hand2:
        print(card['face'], "of", card['suit'])
    print("This hand contains:")
    result_hand2 = test_hand(hand2)
    if result_hand1 < result_hand2:
        print("Hand 1 Wins")
    elif result_hand1 > result_hand2:
        print("Hand 2 Wins")
    else:
        check_same_hand(hand1,hand2)
def check_same_hand(hand1,hand2):
    hand1 = sorted(hand1, key=lambda card: card['value'])
    values1 = []
    for card in hand1:
        values1.append(card['value'])
    hand2 = sorted(hand2, key=lambda card: card['value'])
    values2 = []
    for card in hand2:
        values2.append(card['value'])
    for value1 in values1:
        for value2 in values2:
            if value1 > value2:
                print("Hand 1 Wins")
                return
            elif value2 > value1:
                print("Hand 2 Wins")
                return
if __name__ == '__main__':
    main()