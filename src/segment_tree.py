class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build_tree(1, 0, len(arr) - 1)

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(2 * node, start, mid)
            self.build_tree(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, l, r)
        right_sum = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum


n = int(input())
arr = list(map(int, input().split()))
tree = SegmentTree(arr)
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(tree.query(1, 0, n - 1, l, r))
