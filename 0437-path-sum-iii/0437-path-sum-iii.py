class Solution:
    count = 0
    def pathSum(self, root, targetSum):
        if root == None:
            return 0
            
        def dfs(root, targetSum, sum):
            if root == None:
                return
                
            sum += root.val
            if sum == targetSum:
                self.count += 1
                
            dfs(root.left, targetSum, sum)
            dfs(root.right, targetSum, sum)
            
        dfs(root, targetSum, 0)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.count