from typing import TypeVar

# Used for type hinting within class
TreeNodeType = TypeVar("TreeNodeType", bound="TreeNode")


class TreeNode:
    def __init__(self, name: str, parent: TreeNodeType, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children: dict[str, TreeNodeType] = {}

    def get_size(self) -> int:
        if not self.size:
            for child in self.children.values():
                self.size += child.get_size()
        return self.size

    def set_child(self, child: TreeNodeType):
        self.children[child.name] = child


def buildTree() -> TreeNode:
    root = TreeNode('/', None)
    node = root
    with open('input.txt', 'r') as f:
        next(f)
        while line := f.readline().rstrip():
            params = line.split(' ')
            if line.startswith('$ cd'):
                if params[2] == '..':
                    node = node.parent
                else:
                    node = node.children[params[2]]
            if not line.startswith('$'):
                if params[0] == 'dir':
                    node.set_child(TreeNode(params[1], node))
                else:
                    node.set_child(TreeNode(params[1], node, int(params[0])))
    return root


def recur_solve1(node: TreeNode) -> int:
    count = 0
    for child in node.children.values():
        count += recur_solve1(child)
        if child.children and child.get_size() < 100000:
            count += child.get_size()
    return count


def solve1():
    root = buildTree()
    ans = recur_solve1(root)
    print(ans)


def recur_solve2(node: TreeNode, required_space: int) -> int:
    smallest = 70000000
    for child in node.children.values():
        smallest = min(smallest, recur_solve2(child, required_space))
        if child.children and child.get_size() > required_space:
            smallest = min(smallest, child.get_size())
    return smallest


def solve2():
    root = buildTree()
    used_space = root.get_size()
    free_space = 70000000 - used_space
    space_to_free = 30000000 - free_space
    ans = recur_solve2(root, space_to_free)
    print(ans)


solve1()
solve2()
