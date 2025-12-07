from collections import defaultdict


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    split_count = 0
    beam_ids = []

    for col in range(len(data[0])):
        if data[:1][0][col] == "S":
            beam_ids.append(col)

    for row in data[1:]:
        beam_ids_to_add = []
        beam_ids_to_remove = []

        for remove_beam_id in beam_ids:
            if row[remove_beam_id] == "^":
                beam_ids_to_remove.append(remove_beam_id)

                if (remove_beam_id - 1) not in beam_ids_to_add:
                    beam_ids_to_add.append(remove_beam_id - 1)

                if (remove_beam_id + 1) not in beam_ids_to_remove:
                    beam_ids_to_add.append(remove_beam_id + 1)

                split_count += 1

        for remove_beam_id in beam_ids_to_remove:
            beam_ids.remove(remove_beam_id)

        beam_ids.extend(beam_ids_to_add)

        beam_ids = list(dict.fromkeys(beam_ids))

    return split_count


def solve_part2(data):
    return "sol2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 07 - Part 1: {result1}")
    print(f"Day 07 - Part 2: {result2}")
