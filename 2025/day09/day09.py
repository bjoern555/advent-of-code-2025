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
    points = []

    for line in data:
        col, row = line.split(",")
        points.append((int(col), int(row)))

    green_walls = []

    for i in range(len(points) - 1):
        green_walls.append((points[i], points[i + 1]))

    green_walls.append((points[-1], points[0]))

    max_area = 0

    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue

            w_p1 = points[i]
            w_p2 = points[j]

            r_y_min = min(w_p1[1], w_p2[1])
            r_y_max = max(w_p1[1], w_p2[1])
            r_x_min = min(w_p1[0], w_p2[0])
            r_x_max = max(w_p1[0], w_p2[0])

            valid = True

            for p1, p2 in green_walls:
                w_x1, w_y1 = p1
                w_x2, w_y2 = p2

                w_x_min, w_x_max = min(w_x1, w_x2), max(w_x1, w_x2)
                w_y_min, w_y_max = min(w_y1, w_y2), max(w_y1, w_y2)

                if w_y1 == w_y2:
                    wall_y = w_y1
                    if r_y_min < wall_y < r_y_max:
                        if w_x_min < r_x_max and w_x_max > r_x_min:
                            valid = False
                            break

                elif w_x1 == w_x2:
                    wall_x = w_x1
                    if r_x_min < wall_x < r_x_max:
                        if w_y_min < r_y_max and w_y_max > r_y_min:
                            valid = False
                            break

            if valid:
                width = abs(w_p1[0] - w_p2[0]) + 1
                height = abs(w_p1[1] - w_p2[1]) + 1

                area = width * height

                if area > max_area:
                    max_area = area

    return max_area


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 09 - Part 1: {result1}")
    print(f"Day 09 - Part 2: {result2}")
