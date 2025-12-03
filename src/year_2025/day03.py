
def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    banks = [list(map(int, list(line))) for line in lines]
    largest_batteries = []
    for bank in banks:
        largest_number = sorted(bank[:-1])[-1]
        second_largest = sorted(bank[bank.index(largest_number)+1:])[-1]

        largest_batteries.append(int(str(largest_number) + str(second_largest)))
    
    return sum(largest_batteries)

def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    banks = [list(map(int, list(line))) for line in lines]
    largest_batteries = []
    for bank in banks:

        battery = ""
        start_pos = 0
        numbers_to_fill = 11
        for index in range(12):       
            if numbers_to_fill == 0:
                temp = bank[start_pos:]
            else:
                temp = bank[start_pos:-numbers_to_fill]
                
            largest = max(temp)
      
            start_pos = bank.index(largest, start_pos) + 1
            battery += str(largest)  
            numbers_to_fill -= 1
        largest_batteries.append(int(battery))
    
    return sum(largest_batteries)
