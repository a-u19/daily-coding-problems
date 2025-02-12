def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

    image_height = len(image)
    image_width = len(image[0])
    old_color = image[sr][sc]
    if old_color == color:
        return image

    def dfs(sr:int, sc:int):

        if image[sr][sc] == old_color:
            image[sr][sc] = color

            if sr - 1 >= 0:
                dfs(sr=sr-1, sc=sc)
            if sc + 1 < image_width:
                dfs(sr=sr, sc=sc+1)
            if sr + 1 < image_height:
                dfs(sr=sr+1, sc=sc)
            if sc - 1 >= 0:
                dfs(sr=sr, sc=sc-1)


    dfs(sr, sc)
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))