def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    shortest_points = []

    for point in data:
        x, y, z = map(int, point.split(","))

        for comparison_point in data:
            if comparison_point == point:
                continue

            x2, y2, z2 = map(int, comparison_point.split(","))

            shortest_points.append(
                (
                    (x2 - x) ** 2 + (y2 - y) ** 2 + (z2 - z) ** 2,
                    point,
                    comparison_point,
                )
            )

    shortest_points = sorted(shortest_points)
    shortest_points = [(p1, p2) for _, p1, p2 in shortest_points[::2][:1000]]

    groups = []

    for p1, p2 in shortest_points:
        idx1 = -1
        idx2 = -1

        for i, group in enumerate(groups):
            if p1 in group:
                idx1 = i
            if p2 in group:
                idx2 = i

        if idx1 == -1 and idx2 == -1:
            groups.append([p1, p2])
        elif idx1 != -1 and idx2 == -1:
            groups[idx1].append(p2)
        elif idx1 == -1 and idx2 != -1:
            groups[idx2].append(p1)
        elif idx1 != idx2:
            if idx1 > idx2:
                groups[idx2].extend(groups[idx1])
                groups.pop(idx1)
            else:
                groups[idx1].extend(groups[idx2])
                groups.pop(idx2)

    lengths = sorted([len(g) for g in groups])
    return lengths[-1] * lengths[-2] * lengths[-3]


def solve_part2(data):
    return "sol2"


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 08 - Part 1: {result1}")
    print(f"Day 08 - Part 2: {result2}")
