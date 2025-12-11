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
    node_map = {}
    for line in data:
        node, neighbors = line.split(":")
        neighbors = neighbors.split(" ")[1:]
        node_map[node] = neighbors

    svr_to_fft = count_paths_to_target("svr", "fft", node_map, blocked=["dac", "out"])
    fft_to_dac = count_paths_to_target("fft", "dac", node_map, blocked=["svr", "out"])
    dac_to_out = count_paths_to_target("dac", "out", node_map, blocked=["svr", "fft"])

    svr_to_dac = count_paths_to_target("svr", "dac", node_map, blocked=["fft", "out"])
    dac_to_fft = count_paths_to_target("dac", "fft", node_map, blocked=["svr", "out"])
    fft_to_out = count_paths_to_target("fft", "out", node_map, blocked=["dac", "svr"])

    return svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out


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
