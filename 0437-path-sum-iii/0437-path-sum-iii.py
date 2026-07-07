class Solution:
    def pathSum(self, root, targetSum):
        if root == None:
            return 0
            
        def dfs(root, targetSum, sum, dict1):
            if root == None:
                return 0
                
            count = 0
            sum += root.val
            count += dict1.get(sum - targetSum, 0)
            dict1[sum] = dict1.get(sum, 0) + 1
            
            count += dfs(root.left, targetSum, sum, dict1)
            count += dfs(root.right, targetSum, sum, dict1)
            
            dict1[sum] -= 1
            return count
            
        sum = 0
        dict1 = {0: 1}
        return dfs(root, targetSum, sum, dict1)