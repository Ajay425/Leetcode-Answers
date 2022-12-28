class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res=[]

        def postorder(root):
            if (root==None): #if root is none we simply return an empty list
                return
          
            postorder(root.left) #else we will got to the left 
            postorder(root.right) #calls the function again. We visit everything to the right and append them
            res.append(root.val)
        postorder(root) #calling the root
        return res
        
