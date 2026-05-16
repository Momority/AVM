class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        
        def dfs(current_node):
           
            if current_node in old_to_new:
                return old_to_new[current_node]
            
            copy = Node(current_node.val)
            old_to_new[current_node] = copy
            
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)