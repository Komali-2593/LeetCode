
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0

        # Find all rotten oranges and count fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # Spread rot level by level
        while queue and fresh > 0:
            for _ in range(len(queue)):

                i, j = queue.popleft()

                # up
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh -= 1
                    queue.append((i - 1, j))

                # down
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh -= 1
                    queue.append((i + 1, j))

                # left
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh -= 1
                    queue.append((i, j - 1))

                # right
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh -= 1
                    queue.append((i, j + 1))

            time += 1

        if fresh > 0:
            return -1

        return time
            
        

        