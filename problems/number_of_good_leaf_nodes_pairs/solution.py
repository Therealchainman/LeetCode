# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root, threshold) -> int:
        self.ans = 0
        def dfs(node, d=0):
            if not node:
                return []
            left = dfs(node.left, d+1)
            right = dfs(node.right, d+1)
            # print(left, right)
            # ans = []
            # if node.left is node.right is None:
            #     ans.append(d)
            # O(n^2)
            for d1 in left:
                for d2 in right:
                    cand = d1 - d + d2 - d
                    if cand <= threshold:
                        self.ans += 1
            if len(left) < len(right):
                left, right = right, left
            left.extend(right)
            if node.left is node.right is None:
                left.append(d)
            return left
                        
            # ans.extend(left)
            # ans.extend(right)
            # return ans
        dfs(root)
        return self.ans
            
#         graph = defaultdict(list)
#         mp = {} # node: index
#         self.t = 0
#         leaves = set()
        
#         def dfs(node):
#             # Returns the index of the node
#             if node:
#                 mp[node] = self.t
#                 self.t += 1
                
#                 i_left = dfs(node.left)
#                 i_right = dfs(node.right)
#                 if i_left:
#                     graph[i].append(i_left)
#                     graph[i_left].append(i)
#                 if i_right:
#                     graph[i].append(i_right)
#                     graph[i_right].append(i)
                    
#                 if i_left is i_right is None:
#                     leaves.add(i)
#                 return i
        
#         dfs(root)
#         ans = 0
#         for u in range(self.t):
#             if u in leaves:
#                 queue = deque()
#                 queue.append([u,0])
#                 seen = {u}
#                 ans -= 1
#                 while queue:
#                     node, d = queue.popleft()
#                     if d > threshold:
#                         break
#                     if node in leaves:
#                         ans += 1
#                     for nei in graph[node]:
#                         if nei not in seen:
#                             seen.add(nei)
#                             queue.append([nei, d+1])
                            
#         return ans // 2