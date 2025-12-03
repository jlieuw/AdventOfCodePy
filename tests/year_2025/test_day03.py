import pytest

from src.year_2025.day03 import solve_part1, solve_part2

example_input = """
234234234234278
987654321111111
811111111111119
818181911112111"""

def test_part1_example():

    result = solve_part1(example_input)
    assert result == 357
    print("result = ", result)

def test_part1(read_input):
    input_data = read_input(2025, 3)
    result = solve_part1(input_data)
    assert result == 17412
    print("result = ", result)



def test_part2_example():
    result = solve_part2(example_input)
    assert result == 3121910778619
    print(" result = ", result)

def test_part2(read_input):
    input_data = read_input(2025, 3)
    result = solve_part2(input_data)
    assert result == 172681562473501
    print("result = ", result)
