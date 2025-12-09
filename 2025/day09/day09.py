def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    points = []
    for line in data:
        col, row = line.split(",")
        points.append((int(col), int(row)))

    max_area = 0

    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue

            p1 = points[i]
            p2 = points[j]

            width = abs(p1[0] - p2[0] + 1)
            height = abs(p1[1] - p2[1] + 1)

            area = width * height

            if area > max_area:
                max_area = area

    return max_area


def solve_part2(data):
    return "sol2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 09 - Part 1: {result1}")
    print(f"Day 09 - Part 2: {result2}")
