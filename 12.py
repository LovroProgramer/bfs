from collections import deque

def brojOtoka(grid):
    def bfs(start):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Exclude diagonal directions
        queue = deque([start])
        visited.add(start)

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                bfs((i, j))
                islands += 1

    return islands

# Example usage
grid = [
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(brojOtoka(grid))  # Output: 1
