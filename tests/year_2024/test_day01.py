import pytest

from src.year_2024.day01 import solve_part1, solve_part2


def test_part1_example():
    example_input = """
3   4
4   3
2   5
1   3
3   9
3   3"""
    result = solve_part1(example_input)
    assert result == 11
    print("total distance = ", result)

def test_part1(read_input):
    input_data = read_input(2024, 1)
    result = solve_part1(input_data)
    assert result == 2815556
    print("Simalrity score result = ", result)



def test_part2_example():
    example_input = """
3   4
4   3
2   5
1   3
3   9
3   3"""
    result = solve_part2(example_input)
    assert result == 31
    print("Simalrity score result = ", result)

def test_part2(read_input):
    input_data = read_input(2024, 1)
    result = solve_part2(input_data)
    assert result == 23927637
    print("Simalrity score result = ", result)
