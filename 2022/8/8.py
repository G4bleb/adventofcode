class TreeMap:
    def __init__(self):
        with open('input.txt', 'r') as f:
            self.grid = [[int(el) for el in l.rstrip()] for l in f.readlines()]
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def bigger_tree_right(self, x, y) -> int:
        base = self.grid[y][x]
        steps = 0
        for xray in range(x+1, self.width):
            steps += 1
            if self.grid[y][xray] >= base:
                return steps
        return 0

    def bigger_tree_left(self, x, y) -> int:
        base = self.grid[y][x]
        steps = 0
        for xray in reversed(range(0, x)):
            steps += 1
            if self.grid[y][xray] >= base:
                return steps
        return 0

    def bigger_tree_top(self, x, y) -> int:
        base = self.grid[y][x]
        steps = 0
        for yray in reversed(range(0, y)):
            steps += 1
            if self.grid[yray][x] >= base:
                return steps
        return 0

    def bigger_tree_down(self, x, y) -> int:
        base = self.grid[y][x]
        steps = 0
        for yray in range(y+1, self.height):
            steps += 1
            if self.grid[yray][x] >= base:
                return steps
        return 0

    def count_visible_trees(self) -> int:
        visible_trees = 0
        for y in range(self.height):
            for x in range(self.width):
                if y == 0 or x == 0 or y == self.height-1 or x == self.width-1:
                    visible_trees += 1
                else:
                    if ((not self.bigger_tree_right(x, y)) or
                        (not self.bigger_tree_left(x, y)) or
                        (not self.bigger_tree_top(x, y)) or
                            (not self.bigger_tree_down(x, y))):
                        visible_trees += 1
        return visible_trees

    def scenic_score(self, x, y) -> int:
        tmp = self.bigger_tree_right(x, y)
        right = tmp if tmp else self.width - x - 1
        tmp = self.bigger_tree_left(x, y)
        left = tmp if tmp else x
        tmp = self.bigger_tree_top(x, y)
        top = tmp if tmp else y
        tmp = self.bigger_tree_down(x, y)
        down = tmp if tmp else self.height - y - 1
        return right*left*top*down

    def best_scenic_score(self) -> int:
        best = 0
        for y in range(1, self.height-1):
            for x in range(1, self.width-1):
                best = max(best, self.scenic_score(x, y))
        return best


def solve1() -> None:
    trees = TreeMap()
    print(trees.count_visible_trees())


def solve2() -> None:
    trees = TreeMap()
    print(trees.best_scenic_score())


solve1()
solve2()
