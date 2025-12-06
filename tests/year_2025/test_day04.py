import pytest

from src.year_2025.day04 import solve_part1, solve_part2

example_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def test_part1_example():

    result = solve_part1(example_input)
    assert result == 13
    print("result = ", result)

def test_part1(read_input):
    input_data = read_input(2025, 4)
    result = solve_part1(input_data)
    assert result == 1416
    print("result = ", result)



def test_part2_example():
    result = solve_part2(example_input)
    assert result == 43
    print(" result = ", result)

def test_part2(read_input):
    input_data = read_input(2025, 4)
    result = solve_part2(input_data)
    assert result == 9086
    print("result = ", result)
