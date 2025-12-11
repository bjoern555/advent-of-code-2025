def read_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


def parse_data(raw_data):
    lines = raw_data.split("\n")
    return lines


def solve_part1(data):
    node_map = {}

    for line in data:
        node, neighbors = line.split(":")
        neighbors = neighbors.split(" ")[1:]

        node_map[node] = neighbors

    return count_paths_to_target("you", "out", node_map)


def solve_part2(data):
    return "sol2"


def count_paths_to_target(start, target, node_map, blocked=None):
    if blocked is None:
        blocked = set()
    else:
        blocked = set(blocked)

    memo = {}

    def dfs(current_node):
        if current_node == target:
            return 1

        if current_node in blocked:
            return 0

        if current_node in memo:
            return memo[current_node]

        total_paths = 0

        for neighbor in node_map.get(current_node, []):

            total_paths += dfs(neighbor)

        memo[current_node] = total_paths
        return total_paths

    return dfs(start)


if __name__ == "__main__":
    input_path = "input.txt"

    raw_input = read_input(input_path)
    parsed_data = parse_data(raw_input)

    result1 = solve_part1(parsed_data)
    result2 = solve_part2(parsed_data)

    print(f"Day 11 - Part 1: {result1}")
    print(f"Day 11 - Part 2: {result2}")
