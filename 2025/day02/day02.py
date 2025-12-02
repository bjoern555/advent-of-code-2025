from black import ranges


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    ranges = raw_data.split(",")
    return ranges


def solve_part1(data):
    summed_invalid_ids = 0

    for range_tuple in data:
        start, end = range_tuple.split("-")

        for id in range(int(start), int(end) + 1):
            s = str(id)
            s_len = len(s)

            if s_len % 2 == 0:
                mid = s_len // 2

                part_one = s[:mid]
                part_two = s[mid:]

                if part_one == part_two:
                    summed_invalid_ids += id
    return summed_invalid_ids


def solve_part2(data):
    return "part2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 01 - Part 1: {result1}")
    print(f"Day 01 - Part 2: {result2}")
