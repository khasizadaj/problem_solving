import copy

from config import PATTERN_STRENGTHS, RANKS


def best_hands(hands: list[str]) -> list[str]:
    """
    Picks the best hand(s) from a list of poker hands.
    """
    hands_analysis = [get_hand_analysis(hand) for hand in hands]

    hands_analysis = sorted(hands_analysis, key=lambda x: x["pattern"]["strength"])

    result = hands_analysis[-1]
    # print(f"Result: {result}")
    return [result["hand"]]


def compare_hands(first_hand: str, second_hand: str) -> bool:
    """
    Returns integer values that represents if the first hand is better than
    second hand. If return value is positive, the first hand is better than
    second hand. Otherwise, second hand is better.
    """

    result = False

    pattern_strength_of_first_hand = get_pattern_strength(first_hand["pattern"])
    pattern_strength_of_second_hand = get_pattern_strength(second_hand["pattern"])
    if pattern_strength_of_first_hand > pattern_strength_of_second_hand:
        return 1
    elif pattern_strength_of_first_hand < pattern_strength_of_second_hand:
        return -1

    return result


def get_pattern_strength(pattern: str) -> int:
    """Returns strength number of each pattern."""
    return PATTERN_STRENGTHS[pattern]


def get_hand_analysis(hand: str) -> dict:
    """
    Returns an anlysis of the hand. It counts the suits and ranks of the
    given hand.
    """

    cards = hand.split(" ")

    result = {"hand": hand, "card_analysis": {"suits": {}, "ranks": {}}}
    for card in cards:
        suit = card[-1]

        suit_in_result = result["card_analysis"]["suits"].get(suit, None)
        if suit_in_result is None:
            result["card_analysis"]["suits"][suit] = 1
        else:
            result["card_analysis"]["suits"][suit] += 1

        rank = card[:-1]
        rank_in_result = result["card_analysis"]["ranks"].get(rank, None)
        if rank_in_result is None:
            result["card_analysis"]["ranks"][rank] = 1
        else:
            result["card_analysis"]["ranks"][rank] += 1

    pattern = get_pattern(result["card_analysis"])
    result["pattern"] = {
        "name": pattern,
        "strength": get_pattern_strength(pattern),
    }

    return result


def get_pattern(card_details: dict) -> str:
    """Returns pattern that given hand analysis has."""

    suits: dict = card_details["suits"]
    ranks: dict = card_details["ranks"]
    suit_counts = list(suits.values())
    suit_counts.sort()

    rank_counts = list(ranks.values())
    rank_counts.sort()

    # print(f"Suit counts: {suit_counts}")
    # print(f"Rank counts: {rank_counts}")
    # print(rank_counts)

    result = "High card"
    if rank_counts == [1, 4]:
        result = "Four of a kind"
    elif rank_counts == [2, 3]:
        result = "Full house"
    elif rank_counts == [1, 1, 3]:
        result = "Three of a kind"
    elif rank_counts == [1, 2, 2]:
        result = "Two pair"
    elif rank_counts == [1, 1, 1, 2]:
        result = "One pair"
    elif rank_counts == [1] * 5:
        rank_values = [RANKS[rank] for rank, _ in ranks.items()]
        rank_values.sort()

        is_straight = (rank_values[0] + rank_values[4]) / 2 == rank_values[2]
        is_flush = suit_counts == [5]

        if is_straight and is_flush:
            result = "Straight flush"
        elif is_straight and not is_flush:
            result = "Straight"
        elif is_flush and not is_straight:
            result = "Flush"

    return result


if __name__ == "__main__":
    all_hands = ["4S 4H 4D 4C 3H", "AS AH AC KS KD"]
    best = best_hands(all_hands)
    print(best)
