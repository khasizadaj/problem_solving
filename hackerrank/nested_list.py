Scores = list[list[str, int]]


def get_second_lowest_score(score_table: Scores):
    scores = {result[1] for result in score_table}
    second_lowest = sorted(scores)[1]
    return second_lowest


if __name__ == "__main__":
    score_table = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_table.append([name, score])

    score_table = [
        ["Hina", 20],
        ["Hiena", 19],
        ["Shina", 20],
        ["Mina", 19],
        ["Tina", 21],
    ]
    second_lowest = get_second_lowest_score(score_table)
    print(f"Second lowest: {second_lowest}")
    second_lowest_names = [
        result[0] for result in score_table if result[1] == second_lowest
    ]

    if len(second_lowest_names) > 1:
        second_lowest_names.sort()

    for name in second_lowest_names:
        print(name)
