def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    accessible_rolls = 0

    rows = len(data)
    cols = len(data[0])

    for row in range(rows):
        for col in range(cols):
            if data[row][col] == "@":
                roll_counter = 0

                if row != 0 and col != 0 and data[row - 1][col - 1] == "@":
                    roll_counter += 1
                if row != 0 and data[row - 1][col] == "@":
                    roll_counter += 1
                if row != 0 and col != cols - 1 and data[row - 1][col + 1] == "@":
                    roll_counter += 1
                if col != cols - 1 and data[row][col + 1] == "@":
                    roll_counter += 1
                if (
                    row != rows - 1
                    and col != cols - 1
                    and data[row + 1][col + 1] == "@"
                ):
                    roll_counter += 1
                if row != rows - 1 and data[row + 1][col] == "@":
                    roll_counter += 1
                if row != rows - 1 and col != 0 and data[row + 1][col - 1] == "@":
                    roll_counter += 1
                if col != 0 and data[row][col - 1] == "@":
                    roll_counter += 1

                if roll_counter < 4:
                    accessible_rolls += 1

    return accessible_rolls


def solve_part2(data):
    accessible_rolls = 0

    rows = len(data)
    cols = len(data[0])

    matrix = [list(row) for row in data]

    while True:
        to_remove = []

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "@":
                    roll_counter = 0

                    if row != 0 and col != 0 and matrix[row - 1][col - 1] == "@":
                        roll_counter += 1
                    if row != 0 and matrix[row - 1][col] == "@":
                        roll_counter += 1
                    if row != 0 and col != cols - 1 and matrix[row - 1][col + 1] == "@":
                        roll_counter += 1
                    if col != cols - 1 and matrix[row][col + 1] == "@":
                        roll_counter += 1
                    if (
                        row != rows - 1
                        and col != cols - 1
                        and matrix[row + 1][col + 1] == "@"
                    ):
                        roll_counter += 1
                    if row != rows - 1 and matrix[row + 1][col] == "@":
                        roll_counter += 1
                    if row != rows - 1 and col != 0 and matrix[row + 1][col - 1] == "@":
                        roll_counter += 1
                    if col != 0 and matrix[row][col - 1] == "@":
                        roll_counter += 1

                    if roll_counter < 4:
                        accessible_rolls += 1
                        to_remove.append([row, col])

        if not to_remove:
            break

        for row, col in to_remove:
            matrix[row][col] = "."

    return accessible_rolls


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 04 - Part 1: {result1}")
    print(f"Day 04 - Part 2: {result2}")
