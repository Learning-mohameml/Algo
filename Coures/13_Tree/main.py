from __future__ import annotations
from typing import Optional , List , Literal

class TreeNode : 
    def __init__(self,val=0 , left=None , right=None):
        self.val = val 
        self.left : Optional[TreeNode] = left
        self.right : Optional[TreeNode] = right


    def print(self, indent : str = "" , last = True) -> None :
        
        # Print current node
        print(indent, "└── " if last else "├── ", self.val, sep="")

        # Update indentation for children : 
        indent += "   "  if last else "|  "

        # Print left child
        if self.left:
            # left child is NOT the last if right child exists
            child_is_last = not self.right
            self.left.print(indent, child_is_last)

        # Print right child (always the last)
        if self.right:
            self.right.print(indent, True)

    def height(self) -> int :
        "compute the  maximum depth"
        def _height(tree : Optional[TreeNode]) -> int: 
            
            if not tree : 
                return 0 

            if not tree.left and not tree.right : 
                return 1 

            return 1 + max(_height(tree.left)  , _height(tree.right))
        

        return _height(self)

    def is_same(self ,other : TreeNode) -> bool : 
        "Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."
        def _is_same(tree1 :Optional[TreeNode] , tree2 : Optional[TreeNode]) -> bool :
            if not tree1 and not tree2 : 
                return True 
            
            if not tree1 or not tree2 : 
                return False 
            
            return (
                tree1.val == tree2.val and 
                _is_same(tree1.left , tree2.left) and 
                _is_same(tree1.right ,  tree2.right)
            )


        return _is_same(self , other)

    def is_leaf(self) -> bool : 
        "return if the tree is leaf tree "

        return self.left  is None  and  self.right is None 

    def dfs(
            self,
            methode_type : Literal["rec" , "iter"] = "rec",
            dfs_type : Literal["preorder" , "inorder" ,"postorder"] = "preorder"
        ) -> List :
        """
        - DFS explore un chemin le plus profondément possible avant de revenir en arrière.
        - On va jusqu'à une feuille, puis on remonte.

        - Types : 
            - Preorder : Noeud -> Left -> Right  : [Copie or Serialization]
            - Inorder : Left -> Noeud -> Right  : [use in BST ]
            - PostOrder : Left -> Right -> Noeud : [Supprimer Arbre ]
        
        - Complexité : 
            - Time : O(n)
            - Space : O(h) avec h : hauteur de l'arbre 
        """

        if methode_type == "rec" : 
            return self._dfs_rec(type=dfs_type)
        
        if methode_type == "iter" : 
            return self._dfs_iter(type=dfs_type)

        raise ValueError(f"type '{methode_type}' unknown (expected 'rec' or 'iter')")

    def _dfs_rec(
            self , 
            type : Literal["preorder" , "inorder" ,"postorder"] = "preorder"
        ) -> list : 
        res = []

        def _go(node : Optional[TreeNode]) :
            if not node : 
                return 
            
            match type : 
                case "preorder" : 
                    # Noeud -> Left -> Right
                    res.append(node.val)
                    _go(node.left)
                    _go(node.right)

                case "inorder" : 
                    # Left -> Noeud -> Right
                    _go(node.left)
                    res.append(node.val)
                    _go(node.right)
                case "postorder" : 
                    # Left -> Right -> Noeud
                    _go(node.left)
                    _go(node.right)
                    res.append(node.val)
                
                case _ : 
                    raise ValueError(f"type {type} unkown")


        _go(self)
        return res 

    def _dfs_iter(
        self,
        type : Literal["preorder" , "inorder" ,"postorder"] = "preorder"
    ) -> list : 
        
        match type : 
            case "preorder" : 
                return self._dfs_iter_preorder()
            case "inorder" : 
                return self._dfs_iter_inorder()
            case "postorder" :
                return self._dfs_iter_postorder()
            case _ : 
                raise ValueError(f"type {type} Unkown")

    def _dfs_iter_preorder(
        self
    ) -> list : 
        """Root -> Left -> Right"""
        res = []
        stack : List[TreeNode] = [self]

        while stack : 
            node = stack.pop()
            res.append(node.val)

            if node.right : 
                stack.append(node.right)
            if node.left : 
                stack.append(node.left)
            

        return res 

    def _dfs_iter_inorder(
        self
    ) -> list : 
        """
        - Order : Left -> Root  -> Right
        - Algo : 
            “In inorder traversal, we push nodes while going left, and only process them when we can't go further left.”
        
        """
        res = []
        stack : List[TreeNode] = []
        curr : Optional[TreeNode] = self 

        while curr is not None or stack  : 

            while curr is not None : 
                stack.append(curr)
                curr = curr.left 
            
            node = stack.pop()
            res.append(node.val)
            curr = node.right

        return res 

    def _dfs_iter_postorder(self) -> list :
        """
        - Order : Left -> Right -> Root
        - Algo : 
            - “In postorder traversal, a node is processed only after both subtrees are fully visited.”
        """
        
        res = []
        stack : List[TreeNode] = []
        curr : Optional[TreeNode] = self 
        last_visited : Optional[TreeNode] = None 


        while curr is not None or stack : 
            while curr is not None : 
                stack.append(curr)
                curr = curr.left 


            peek = stack[-1]
            if peek.right is not None and last_visited != peek.right : 
                curr = peek.right 
            else : 
                res.append(peek.val)
                last_visited = stack.pop()
                curr = None 


        return res 

