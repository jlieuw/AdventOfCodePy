
def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    max_x = len(lines[0])
    max_y = len(lines)

    paper_locations = set()
    for y, line in enumerate(lines):
        for x, paper_location in enumerate(list(line)):
            if paper_location == '@':
                paper_locations.add((x, y))

    

    return remove_rolls_of_paper(paper_locations, max_x, max_y, 0, False)

def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")
    max_x = len(lines[0])
    max_y = len(lines)

    paper_locations = set()
    for y, line in enumerate(lines):
        for x, paper_location in enumerate(list(line)):
            if paper_location == '@':
                paper_locations.add((x, y))
    
    return remove_rolls_of_paper(paper_locations, max_x, max_y, 0, True)

def remove_rolls_of_paper(paper_locations: list, max_x: int, max_y: int, paper_removed: int, part2: bool) -> int:
    to_remove = set()
    for x, y in paper_locations:
        neighbours = list(get_neighbors(x, y, max_x, max_y))
        count = len([n for n in neighbours if n in paper_locations])
        if count < 4:
            to_remove.add((x, y))
            
    if not to_remove: 
        return paper_removed
        
    paper_locations -= to_remove
    paper_removed += len(to_remove)
    
    if part2:
        return remove_rolls_of_paper(paper_locations, max_x, max_y, paper_removed, part2)
    
    return paper_removed

def get_neighbors(x, y, max_x, max_y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y:
                yield (nx, ny)