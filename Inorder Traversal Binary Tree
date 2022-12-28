class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res=[] #store the values every time we visit a node

        def preorder(root):
            if (root==None): #if root is none we simply return an empty list
                return
                        
            res.append(root.val) #we start inserting the value
            preorder(root.left) # calls the function.we will got to the left 
            preorder(root.right) #calls the function again. We visit everything to the right and append them
        preorder(root) #calling the root.
        return res
            
