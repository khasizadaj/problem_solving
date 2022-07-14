"""
Explanation will be added.
"""

# link tp problem: https://www.hackerrank.com/challenges/most-commons/problem

LetterResult = list[str, int]
ListOfLetterResults = list[LetterResult]


def get_most_commons(word: str, quantity: int = 3) -> ListOfLetterResults:
    """Returns most common letters of the word with the given quantity."""

    count_of_letters = count(word)

    # sorting results alphabetically and reversing it.
    # reverse is needed to comply with requirement of the problem, that is
    # to chosse alphabetically smaller letter if count is the same.
    count_of_letters.sort(key=lambda x: x[0], reverse=True)

    result = collect_most_occured(count_of_letters, quantity)
    result.sort(key=lambda x: x[1], reverse=True)
    return result


def collect_most_occured(count_of_letters: ListOfLetterResults, quantity: int):
    """Function collects most occured letter results given the quantoty."""

    result = []

    for _ in range(quantity):
        curr_highest_result = ["", 0]
        for curr_result in count_of_letters:
            if curr_result[1] >= curr_highest_result[1]:
                curr_highest_result = curr_result

        count_of_letters.remove(curr_highest_result)
        result.append(curr_highest_result)

    return result


def count(word: str) -> ListOfLetterResults:
    """Count letters of the word."""

    # sorted_word: list = sorted(word, reverse=True)
    list_of_unique_letters = sorted(set(word), reverse=True)

    return [[letter, word.count(letter)] for letter in list_of_unique_letters]


if __name__ == "__main__":
    test_most_commons = get_most_commons("google")
    real_most_commons = [["g", 2], ["o", 2], ["e", 1]]
    assert test_most_commons == real_most_commons

    for result in test_most_commons:
        print(f"{result[0]} {result[1]}")

    test_most_commons_2 = get_most_commons("aabbbccceddddfghijklmnopqrstuvwxyz")
    real_most_commons_2 = [["d", 4], ["b", 3], ["c", 3]]
    assert test_most_commons_2 == real_most_commons_2

    for result in test_most_commons_2:
        print(f"{result[0]} {result[1]}")

    sum = lambda x, y: x + y
    print(sum(5, 7))

    # let sum = (x, y) => return x + y;
