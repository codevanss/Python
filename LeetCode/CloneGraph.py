# Definition for a Node.
class Node:
    def __init__(self , val=0 , neighbors = None):
        self.val = val 
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self , node:'Node'):
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# 1 -- 2
# |    |
# 4 -- 3

# Connect neighbors (undirected)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph
sol = Solution()
cloned_node = sol.cloneGraph(node1)

# Check the result
print(cloned_node.val)                     # 1
print([n.val for n in cloned_node.neighbors])  # [2, 4]
print([n.val for n in cloned_node.neighbors[0].neighbors]) # [1, 3]
