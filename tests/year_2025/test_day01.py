import pytest

from src.year_2025.day01 import solve_part1, solve_part2


def test_part1_example():
    example_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    result = solve_part1(example_input)
    assert result == 3
    print("result = ", result)

def test_part1(read_input):
    input_data = read_input(2025, 1)
    result = solve_part1(input_data)
    assert result == 969
    print("result = ", result)



def test_part2_example():
    example_input = """
L112
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    result = solve_part2(example_input)
    assert result == 6
    print(" result = ", result)

def test_part2(read_input):
    input_data = read_input(2025, 1)
    result = solve_part2(input_data)
    assert result == 5887
    print("result = ", result)
