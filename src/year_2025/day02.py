import re

def solve_part1(input_data: str) -> int:
    ranges = input_data.split(",")
    ranges_list = [range.strip().split("-") for range in ranges]
    
    invalid_ids = []
    for ranges in ranges_list:
        for i in range(int(ranges[0]), int(ranges[1])+1):
            str_i = str(i)
            len_i = len(str_i)
            if len_i % 2 == 0:
                middle = len_i // 2
                first_half = str_i[:middle]
                second_half = str_i[middle:]
                if first_half == second_half:
                    invalid_ids.append(i)

    return sum(invalid_ids)  

def solve_part2(input_data: str) -> int:
    ranges = input_data.split(",")
    ranges_list = [range.strip().split("-") for range in ranges]
    
    invalid_ids = []
    for ranges in ranges_list:
        for i in range(int(ranges[0]), int(ranges[1])+1):
            str_i = str(i)
            match = re.match(r'^(.+?)\1+$', str_i)
            if match:
                    invalid_ids.append(i)


    return sum(invalid_ids)  