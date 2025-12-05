def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    separator_index = data.index("")

    fresh_range_lines = data[:separator_index]
    ingredient_id_lines = data[separator_index + 1 :]

    fresh_intervals = []

    for raw_interval in fresh_range_lines:
        start_str, end_str = raw_interval.split("-")
        fresh_intervals.append((int(start_str), int(end_str)))

    fresh_ids = 0

    for ingredient_id_str in ingredient_id_lines:
        ingredient_id = int(ingredient_id_str)

        for start, end in fresh_intervals:
            if start <= ingredient_id <= end:
                fresh_ids += 1
                break

    return fresh_ids


def solve_part2(data):

    ranges = []

    for line in data:
        if line == "":
            break
        start_str, end_str = line.split("-")
        ranges.append((int(start_str), int(end_str)))

    ranges.sort()

    merged_range = list(ranges[0])
    fresh_ids = 0

    for range_tuple in ranges[1:]:
        start, end = range_tuple

        if end <= merged_range[1]:
            continue
        elif start <= merged_range[1]:
            merged_range[1] = end
        else:
            fresh_ids += merged_range[1] - merged_range[0] + 1
            merged_range = [start, end]

    fresh_ids += merged_range[1] - merged_range[0] + 1

    return fresh_ids


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 05 - Part 1: {result1}")
    print(f"Day 05 - Part 2: {result2}")
