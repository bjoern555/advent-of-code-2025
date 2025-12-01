# 2025/day01/day01.py


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    return "Part 1 Solution"


def solve_part2(data):
    return "Part 2 Solution"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 01 - Part 1: {result1}")
    print(f"Day 01 - Part 2: {result2}")
