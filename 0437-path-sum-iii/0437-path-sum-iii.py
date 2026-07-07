class Solution:
    def pathSum(self, root, targetSum):
        if root == None:
            return 0
            
        def dfs(root, targetSum, sum):
            if root == None:
                return 0
                
            count = 0
            sum += root.val
            if sum == targetSum:
                count = 1
                
            count += dfs(root.left, targetSum, sum)
            count += dfs(root.right, targetSum, sum)
            
            return count
            
        count = 0
        count += dfs(root, targetSum, 0)
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        
        return count