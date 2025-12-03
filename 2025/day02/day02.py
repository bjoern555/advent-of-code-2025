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
    summed_invalid_ids = 0

    for range_str in data:
        start_str, end_str = range_str.split("-")
        start_id = int(start_str)
        end_id = int(end_str)

        for current_id in range(start_id, end_id + 1):
            s = str(current_id)
            s_len = len(s)

            max_pattern_length = s_len // 2

            for pattern_len in range(1, max_pattern_length + 1):
                if s_len % pattern_len == 0:

                    pattern = s[:pattern_len]
                    num_repetitions = s_len // pattern_len

                    expected_string = pattern * num_repetitions

                    if expected_string == s:
                        summed_invalid_ids += current_id
                        break

    return summed_invalid_ids


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 02 - Part 1: {result1}")
    print(f"Day 02 - Part 2: {result2}")
