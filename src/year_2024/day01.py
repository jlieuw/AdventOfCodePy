
def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    pairs = [list(map(int, line.split())) for line in lines]

    left_column = sorted([pair[0] for pair in pairs])
    right_column = sorted([pair[1] for pair in pairs])

    distances = [abs(number - right_column[index]) for index, number in enumerate(left_column)]

    return sum(distances)

def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    pairs = [list(map(int, line.split())) for line in lines]

    left_column = [pair[0] for pair in pairs]
    right_column = [pair[1] for pair in pairs]

    similarity_score = [number * right_column.count(number) for number in left_column]
    # for number in left_column:
    #     count = right_column.count(number)
    #     similarity_score.append(number * count)
    return sum(similarity_score)