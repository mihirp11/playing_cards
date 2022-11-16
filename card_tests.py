def is_straight_flush(hand):
    if is_flush(hand) and is_straight(hand):
        return True
    else:
        return False
def is_straight(hand):
    suits = []
    for card in hand:
        suits.append(card['suit'])
    original_suit = suits[0]
    for suit in suits:
        if original_suit != suit:
            break
        else:
            return False
    hand = sorted(hand, key=lambda card: card['value'])
    chk = True
    values =[]
    for card in hand:
        values.append(card['value'])
    prev_value = values[0]
    for value in values[1:5]:
        if prev_value + 1 != value:
            chk = False
            break
        else:
            prev_value = value
    return chk
def is_flush(hand):
    hand = sorted(hand, key=lambda card: card['value'])
    values =[]
    for card in hand:
        values.append(card['value'])
    prev_value = values[0]
    for value in values[1:5]:
        if prev_value + 1 != value:
            break
        elif prev_value + 1 == value:
            prev_value = value
        else:
            return False
    suits = []
    for card in hand:
        suits.append(card['suit'])
    original_suit = suits[0]
    chk = True
    for suit in suits:
        if original_suit != suit:
            chk = False
            break
    return chk
def is_3_of_a_kind(hand):
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    if sorted(value_counts.values())==[1,1,3]:
        return True
    else:
        return False
def is_4_of_a_kind(hand):
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    if sorted(value_counts.values())==[1,4]:
        return True
    else:
        return False
def is_2_pair(hand):
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False
def is_pair(hand):
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    if sorted(value_counts.values())==[1,1,1,2]:
        return True
    else:
        return False
def is_full_house(hand):
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    if sorted(value_counts.values())==[2,3]:
        return True
    else:
        return False
def is_high_card(hand):
    if is_flush(hand) or is_straight(hand):
        return False
    values =[]
    for card in hand:
        values.append(card['value'])
    value_counts = {}
    for v in values:
        if v not in value_counts:
            value_counts[v] = 1
        else:
            value_counts[v]+=1
    for v in value_counts:
        if value_counts[v] > 1:
            return False
    return True