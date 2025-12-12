def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    sol = 0

    for line in data:
        pattern = line.split("]")[0][1:]
        pattern_len = len(pattern)
        binary_pattern = 0

        for i in range(pattern_len):
            if pattern[i] == "#":
                binary_pattern += 2 ** (pattern_len - 1 - i)

        switches = line.split(" ")[1:-1]
        numbers = []

        for switch in switches:
            switch = switch.replace("(", "").replace(")", "")
            indexes = switch.split(",")
            number = 0
            for val in indexes:
                number += 2 ** (pattern_len - int(val) - 1)
            numbers.append(number)

        if binary_pattern in numbers:
            sol += 1
            continue

        numbers_map = {num: 1 for num in numbers}

        current_sums = list(numbers_map.keys())
        combinations = 2
        found = False

        while True:

            new_sums_to_add = {}

            for existing_sum in current_sums:
                for new_switch in numbers:

                    new_sum = existing_sum ^ new_switch

                    if new_sum == binary_pattern:
                        sol += combinations
                        found = True
                        break

                    if new_sum not in numbers_map:
                        new_sums_to_add[new_sum] = combinations
                if found:
                    break

            if found:
                break

            if not new_sums_to_add:
                break

            numbers_map.update(new_sums_to_add)
            current_sums = list(new_sums_to_add.keys())
            combinations += 1

    return sol


def solve_part2(data):
    return "was not able to do it"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 10 - Part 1: {result1}")
    print(f"Day 1o - Part 2: {result2}")
