import math


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    dial_size = 100
    dial_position = 50
    zero_dial_count = 0

    for line in data:
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            turning_amount = amount
        else:
            turning_amount = -amount

        dial_position = (dial_position + turning_amount) % dial_size

        if dial_position == 0:
            zero_dial_count += 1

    return zero_dial_count


def solve_part2(data):
    dial_size = 100
    dial_position = 50
    zero_dial_count = 0

    for line in data:
        direction = line[0]
        amount = int(line[1:])
        passed_zeroes = 0

        if direction == "R":
            if dial_position + amount >= dial_size:
                passed_zeroes = math.floor((dial_position + amount) / dial_size)
                dial_position = (dial_position + amount) % dial_size

                if dial_position == 0:
                    passed_zeroes -= 1
            else:
                dial_position = dial_position + amount
        else:
            if dial_position - amount < 0:
                passed_zeroes = math.ceil((amount - dial_position) / dial_size)

                if dial_position == 0:
                    passed_zeroes -= 1

                dial_position = (dial_position - amount) % dial_size
            else:
                dial_position = dial_position - amount

        if dial_position == 0:
            zero_dial_count += 1

        zero_dial_count += passed_zeroes

    return zero_dial_count


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 01 - Part 1: {result1}")
    print(f"Day 01 - Part 2: {result2}")
