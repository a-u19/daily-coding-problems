def dfs(grid: list[list[int]], x: int, y: int, prev_num: int, new_num: int) -> None:
    if grid[x][y] != prev_num:
        return

    grid[x][y] = new_num

    grid_height = len(grid)
    grid_width = len(grid[0])

    if x - 1 > 0:
        dfs(grid=grid, x=x-1, y=y, prev_num=prev_num, new_num=new_num)
    if y + 1 < grid_width:
        dfs(grid=grid, x=x, y=y+1, prev_num=prev_num, new_num=new_num)
    if x + 1 < grid_height:
        dfs(grid=grid, x=x+1, y=y, prev_num=prev_num, new_num=new_num)
    if y - 1 >= 0:
        dfs(grid=grid, x=x, y=y-1, prev_num=prev_num, new_num=new_num)


def flood_fill(grid:list[list[int]], x:int, y:int, new_num:int) -> None:
    prev_num = grid[x][y]
    if prev_num == new_num:
        return
    dfs(grid, x, y, prev_num, new_num)


def highestPeak(isWater: list[list[int]]) -> list[list[int]]:
    flood_fill(isWater, )


highestPeak([[0,1],[0,0]])