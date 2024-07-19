class IntervalTreeNode:
    """
    A node in the Interval Tree, representing a range of values with median-based partitioning.
    """
    def __init__(self, median, crossing_left, crossing_right):
        self.median = median
        self.left = None
        self.right = None
        self.crossing_left = crossing_left
        self.crossing_right = crossing_right


class IntervalTree:
    """
    Data structure to efficiently find all intervals that overlap with any given point or interval.
    """
    def __init__(self, intervals):
        self.root = self.build_tree(intervals)

    def build_tree(self, intervals):
        """Recursively build the interval tree from a list of intervals."""
        if not intervals:
            return None

        # Calculate median
        endpoints = sorted(p for interval in intervals for p in interval)
        median = endpoints[len(endpoints) // 2]

        # Create partitions
        left, right, crossing = [], [], []
        for start, end in intervals:
            if end < median:
                left.append((start, end))
            elif start > median:
                right.append((start, end))
            else:
                crossing.append((start, end))

        # Sort partitions
        crossing_left = sorted(crossing, key=lambda x: x[0])
        crossing_right = sorted(crossing, key=lambda x: x[1], reverse=True)

        # Create tree node
        node = IntervalTreeNode(median, crossing_left, crossing_right)

        # Recursively build left and right subtree
        node.left = self.build_tree(left)
        node.right = self.build_tree(right)

        return node

    def query(self, q, node=None):
        """Query the tree for intervals containing the point q, starting from the node (or root by default)."""
        if node is None:
            node = self.root

        result = []
        if q < node.median:
            for i in node.crossing_left:
                if i[0] <= q <= i[1]:
                    result.append(i)
                else:
                    break
            if node.left:
                result += self.query(q, node.left)
        elif q > node.median:
            for i in node.crossing_right:
                if i[0] <= q <= i[1]:
                    result.append(i)
                else:
                    break
            if node.right:
                result += self.query(q, node.right)
        else:
            result += node.crossing_left

        return result
