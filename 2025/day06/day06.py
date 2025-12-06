def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    parsed_lines = [line.split() for line in data]

    operators = parsed_lines[-1]
    filtered_numbers = parsed_lines[:-1]

    total_sum = 0

    i = 0
    for operator in operators:

        if operator == "+":
            column_result = 0
        else:
            column_result = 1

        for column in filtered_numbers:
            if operator == "+":
                column_result += int(column[i])
            else:
                column_result *= int(column[i])

        i += 1
        total_sum += column_result

    return total_sum


def solve_part2(data):
    return "sol2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 06 - Part 1: {result1}")
    print(f"Day 06 - Part 2: {result2}")
