import math

def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    
    position:int = 50
    counter = 0
    for line in lines:
        direction = line[0]
        turns = int(line[1:])

        if direction == "R":
            new_position = (position + turns) % 100
        elif direction == "L":
            new_position = (position - turns) % 100
        if new_position == 0:
            counter += 1
        
        position = new_position


    return counter

def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    
    position:int = 50
    counter = 0
    for line in lines:
        direction = line[0]
        turns = int(line[1:])

        full_rotations = turns // 100
        counter += full_rotations
        left_over_turns = turns % 100
        if direction == "R":
            temp_position = (position + left_over_turns)
            if temp_position > 100 and temp_position % 100 != 0 and position != 0:
                counter += 1
        elif direction == "L":
            temp_position = (position - left_over_turns)
            if temp_position <= 0 and temp_position % 100 != 0 and position != 0:
                counter += 1

        new_position = temp_position % 100
        if new_position == 0:
            counter += 1
        
        
        position = new_position


    return counter