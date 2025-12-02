import pytest

from src.year_2025.day02 import solve_part1, solve_part2

example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

def test_part1_example():

    result = solve_part1(example_input)
    assert result == 1227775554
    print("result = ", result)

def test_part1(read_input):
    input_data = read_input(2025, 2)
    result = solve_part1(input_data)
    assert result == 28844599675
    print("result = ", result)



def test_part2_example():
    result = solve_part2(example_input)
    assert result == 4174379265
    print(" result = ", result)

def test_part2(read_input):
    input_data = read_input(2025, 2)
    result = solve_part2(input_data)
    assert result == 48778605167
    print("result = ", result)
