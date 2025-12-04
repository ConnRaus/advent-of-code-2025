with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

grid = []
for line in lines:
    grid.append([1 if c == '@' else 0 for c in line])

def count_neighbors(grid, x, y):
    neighborSpots = [(-1, -1), (0, -1), (1, -1),
                     (-1,  0),          (1,  0),
                     (-1,  1), (0,  1), (1,  1)]
    neighbors = 0
    for shift in neighborSpots:
        # if location is in grid
        if 0 <= x + shift[0] <= len(grid[0])-1 and 0 <= y + shift[1] <= len(grid)-1:
            neighbors += grid[y+shift[1]][x+shift[0]]
    return neighbors

result = 0
previous = -1
while True:
    newgrid = [row[:] for row in grid] 
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1 and count_neighbors(grid, j, i) < 4:
                result += 1
                newgrid[i][j] = 0
    
    if previous == result:
        break

    previous = result
    grid = [row[:] for row in newgrid]

print(result)
