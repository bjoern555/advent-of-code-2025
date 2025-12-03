def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    total_output_joltage = 0

    for line_str in data:
        first_digit_max = -1
        first_digit_max_index = -1

        for i in range(len(line_str) - 1):
            if int(line_str[i]) == 9:
                first_digit_max = 9
                first_digit_max_index = i
                break

            if int(line_str[i]) > first_digit_max:
                first_digit_max = int(line_str[i])
                first_digit_max_index = i

        second_digit_max = -1

        for i in range(first_digit_max_index + 1, len(line_str)):
            if int(line_str[i]) == 9:
                second_digit_max = 9
                break

            if int(line_str[i]) > second_digit_max:
                second_digit_max = int(line_str[i])

        total_output_joltage += first_digit_max * 10 + second_digit_max

    return total_output_joltage


def solve_part2(data):
    return "sol2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 03 - Part 1: {result1}")
    print(f"Day 03 - Part 2: {result2}")
