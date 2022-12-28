class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> List[int]:
      
      if(root==None):
        return None
      
      temp=root.left
      root.right=root.left
      root.right=temp
      
      self.invertTree(root.left)
      self.invertTree(root.right)
      
      return root
    
   

        
