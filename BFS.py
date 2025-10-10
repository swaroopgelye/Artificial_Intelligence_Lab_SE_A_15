def dfs_path(maze, start, end):
    stack = [(start, [start])]  # Each item: (current_position, path_so_far)
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path  # Return the path if end is reached

        visited.add((x, y))

        # Explore neighbors: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy

            # Check boundaries, walls, and visited cells
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                stack.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # No path found

# Example maze: 0 = path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

# Run the DFS path-finder
path = dfs_path(maze, start, end)

# Output result
if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")

