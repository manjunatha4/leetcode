from collections import deque

def rotting(grid):
    rows = len(grid)
    c = len(grid[0])
    pr = deque()
    count = 0

    for i in range(rows):
        for j in range(c):
            if grid[i][j] == 2:
                pr.append((i, j))
            elif grid[i][j] == 1:
                count += 1

    d = [(0,-1),(0,1),(-1,0),(1,0)]
    time = 0

    while pr and count > 0:
        for _ in range(len(pr)):
            r, c = pr.popleft()
            for dr, dc in d:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    pr.append((nr, nc))
                    count -= 1
        time += 1

    return time if count == 0 else -1


grid = [[2,1,1],[1,0,1],[2,0,2]]
print(rotting(grid))