def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    shapes = {}
    puzzles = []
    current_id = None

    for line in data:
        if not line:
            continue

        if ":" in line and "x" in line:
            dimensions, counts = line.split(":")
            w, h = dimensions.split("x")
            w = int(w)
            h = int(h)

            reqs = counts.split()
            puzzles.append({"w": w, "h": h, "reqs": reqs})
            current_id = None

        elif line.endswith(":"):
            current_id = int(line[:-1])
            shapes[current_id] = {"grid": [], "area": 0}

        elif current_id is not None:
            row = [1 if c == "#" else 0 for c in line]
            shapes[current_id]["grid"].append(row)
            shapes[current_id]["area"] += sum(row)

    fitting_regions = 0

    for puzzle_idx, puzzle in enumerate(puzzles):

        puzzle_pieces = []
        total_pieces_area = 0
        total_puzzle_area = puzzle["w"] * puzzle["h"]

        for shape_id, count in enumerate(puzzle["reqs"]):
            for _ in range(int(count)):
                shape_data = shapes[shape_id]
                puzzle_pieces.append(shape_data)
                total_pieces_area += shape_data["area"]

        if total_puzzle_area < total_pieces_area:
            continue
        else:
            fitting_regions += 1

    return fitting_regions


def solve_part2(data):
    return "Can't do part 2 because I can't solve day 10 part 2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 12 - Part 1: {result1}")
    print(f"Day 12 - Part 2: {result2}")
