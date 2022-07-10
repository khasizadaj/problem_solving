from poker import get_hand_analysis, get_pattern

HANDS = {
    "Four of a kind": "4S 4H 4D 4C 3H",
    "Full house": "AS AH AC KS KD",
    "Straight flush": "10H JH QH KH AH",
    "Straight": "10D JH QH KC AH",
    "Flush": "8H JH QH KH AH",
    "Three of a kind": "5H 5D 5C KH QH",
    "Two pair": "4S 4H 5D 7S 5D",
    "One pair": "4C 4H 6D 7S 8D",
    "High card": "4C 5H 6D 7S 8D",
}

if __name__ == "__main__":
    analysis = get_hand_analysis(HANDS["Four of a kind"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Four of a kind"
    analysis = get_hand_analysis(HANDS["Full house"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Full house"

    analysis = get_hand_analysis(HANDS["Straight flush"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Straight flush"

    analysis = get_hand_analysis(HANDS["Flush"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Flush"

    analysis = get_hand_analysis(HANDS["Three of a kind"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Three of a kind"

    analysis = get_hand_analysis(HANDS["Two pair"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "Two pair"

    analysis = get_hand_analysis(HANDS["One pair"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "One pair"

    analysis = get_hand_analysis(HANDS["High card"])
    # print(analysis)
    pattern = analysis["pattern"]["name"]
    assert pattern == "High card"
