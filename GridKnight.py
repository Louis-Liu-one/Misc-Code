
dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]


def isvalid(i, j):
    return 0 <= i < height and 0 <= j < width


def dfs(grid, i, j, left):
    if not left:
        return [[(i, j)]]
    res = []
    for di, dj in zip(dx, dy):
        if isvalid(i + di, j + dj) and not grid[i + di][j + dj]:
            grid[i + di][j + dj] = True
            steps = dfs(grid, i + di, j + dj, left - 1)
            grid[i + di][j + dj] = False
            for s in steps:
                res.append([(i, j)] + s)
    return res


def main():
    global width, height
    width, height, x, y = (int(i) for i in input().split())
    grid = [[False] * width for i in range(height)]
    grid[x][y] = True
    steps = dfs(grid, x, y, width * height - 1)
    print(len(steps), steps)


if __name__ == '__main__':
    main()
