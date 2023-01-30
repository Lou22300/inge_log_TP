# encoding utf-8

"""This program permits to create binary trees. We can add nodes, calculate the depth
and display the tree from a chosen node."""

from collections import deque

class BinaryTree() :
    """This class permits to create the root of a binary tree."""
    def __init__(self) :
        """"Initialization of the tree."""
        self.root = None

    def tree_depth(self) :
        """Returns the max depth in the tree."""
        return self.root.find_depth()

    def tree_size(self) :
        """Returns the size of the tree = total nodes number."""
        return self.root.find_size()

    def tree_left_right(self) :
        """Displaying the tree from the root to the end, from left to right."""
        return self.root.display_left_right()

    def tree_up_down(self) :
        """Displaying the tree from the root to the end, from up to down."""
        return self.root.display_up_down()

class Node() :
    """This class permits to add nodes to a biinary tree. We can add only one node to the
    right or the left, or we can add both. The node has to be created before to be added.
    The depth of a new node is automaticaly updated while added to the tree. We can display
    all the nodes from a chosen one. And we can print the tree derived from a node from two
    diffrent methods."""

    def __init__(self, value) :
        """This method permits to create a new node. It takes in argument the value of the node."""
        self.left = None
        self.right = None
        self.depth = 0
        self.value = value

    def add_node(self, left = None, right = None) :
        """This methods permits to add nodes to another one. We can add only one of the left
        and right nodes, or both. The depth of the new nodes is automaticaly changed."""
        self.left = left
        self.right = right
        if self.left :
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right :
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self) :
        """This methods, called in the add_node methods, permits to update the children nodes
        depth. If the added node already has left and right nodes, all the following nodes will
        have there depth updated."""
        if self.left :
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right :
            self.right.depth = self.depth + 1
            self.right.update_children_depth()
        # pass is used so that there is no return -> not returning None.
        # pass

    def display_node(self) :
        """This method is used to display all the nodes deriving from another one. This method
        does not return a tree, only the nodes are printed one by one."""
        retour = str(self)
        if self.left :
            retour += " " + self.left.display_node()
        if self.right :
            retour += " " + self.right.display_node()
        return retour

    def display_left_right(self, level = 0) :
        """This methods is used to display the tree from the left to the right. It uses recursion
        to increase the level in the tree. The level is first set to 0."""
        tree = str(self)
        if self.left :
            tree += "\n"
            for _ in range(0, level+1) :
                tree += "\t"
            tree += self.left.display_left_right(level+1)
        if self.right :
            tree += "\n"
            for _ in range(0, level+1) :
                tree += "\t"
            tree += self.right.display_left_right(level+1)
        return tree

    def dico_for_up_down(self) :
        """This methods is used to create a dictionnary containing the tree. The dictionnary keys
        goes from 0 to the max_depth of the tree. Considering that this is a binary tree, we have
        got all the nodes corresponding to a depth in the value list of any key, with adding a tab
        in every place there is no node. The method is called in the display_up_down method."""
        # Creates an empty dictionnary that will contain the nodes per levels :
        max_depth = self.find_depth()
        dico = {}
        for k in range(max_depth+1) :
            dico[k] = []
        # Create an empty queue (using the collection library) :
        queue = deque()
        # Add the root node to the queue :
        queue.append(self)
        # For each level of the tree :
        for i in range(max_depth+1) :
            # Get the number of nodes in the queue
            nodes_number = len(queue)
            # Loop through the nodes at the current level :
            for _ in range(nodes_number) :
                # Remove the first node from the queue :
                current_node = queue.popleft()
                # Put the node in the dictionnary :
                dico[i].append(str(current_node))
                # If the element in the queue is a node :
                if isinstance(current_node, Node) :
                    # If the current node has a left child, add it to the queue :
                    if current_node.left :
                        queue.append(current_node.left)
                    else : # Else, add a tab :
                        queue.append(" () ")
                    # If the current node has a right child, add it to the queue :
                    if current_node.right :
                        queue.append(current_node.right)
                    else : # Else, add a tab :
                        queue.append(" () ")
                # If the element in the queue is "\t" :
                else :
                    queue.append(" () ") # for the missing left child
                    queue.append(" () ") # for the missing right child
        return dico

    def display_up_down(self) :
        """This method is used to print the tree for up to down. It calls the dico_for_up_down
        method to create a dictionnary containing all the nodes of the tree per level. It prints
        the tree level by level."""
        # Creates the dict that contains the nodes :
        dico = self.dico_for_up_down()
        # Creates the list of the number of tab between nodes :
        space_number_list = []
        for i in range(0,len(dico.keys())) :
            space_number_list.append(int(100/2**i)-2) # cleanest print i found
        # Creates a list that contains the space between nodes :
        white_space_list = space_number_list # same length
        for index, element in enumerate(space_number_list) :
            new_space = " "*element
            white_space_list[index] = new_space
        # Initialize the tree as string :
        tree = ""
        # Displays the tree level by level :
        for level in range(len(dico)) :
            for val in dico[level] :
                new_line = white_space_list[level] + val + white_space_list[level]
                tree += new_line
            tree += "\n"
        return tree

    def find_size(self, nodes_number = 1) :
        """This method is used to find the size of a tree : total number of nodes."""
        if self.left :
            nodes_number += 1
            nodes_number = self.left.find_size(nodes_number)
        if self.right :
            nodes_number += 1
            nodes_number = self.right.find_size(nodes_number)
        return nodes_number

    def is_leaf(self) :
        """This methods is used to know if we are at the end of a branch or if there is still
        at least another node after the actual one. The method is called in the find_depth method.
        It returns a boolean."""
        return self.left is None and self.right is None

    def find_depth(self, max_depth = 0) :
        """This method is used to find the maximum depth of a tree. It takes an optional argument
        which is the maximum depth."""
        # if the node is a leaf (end of a branch) :
        if self.is_leaf() :
            # and if its depth is > actual max_depth
            if self.depth > max_depth :
                return self.depth
        # if the node is not a leaf :
        # recursion is used on the child nodes with a new max_depth until it is a leaf
        if self.right :
            max_depth = self.right.find_depth(max_depth)
        if self.left :
            max_depth = self.left.find_depth(max_depth)
        # when all the tree has been verified, we have the max_depth
        return max_depth

    def __str__(self) -> str:
        """This method is used to print the nodes. It returns 'value/depth' of the node."""
        return str(self.value) + "/" + str(self.depth)

if __name__ == "__main__" :
    # creation of the nodes :
    node1 = Node("01")
    node2 = Node("02")
    node3 = Node("03")
    node4 = Node("04")
    node5 = Node("05")
    node6 = Node("06")
    node7 = Node("07")
    node8 = Node("08")
    node9 = Node("09")
    node10 = Node("10")
    node11 = Node("11")
    node12 = Node("12")
    node13 = Node("13")
    node14 = Node("14")
    node15 = Node("15")
    # creation of the tree starting with the first node as root :
    tree1 = BinaryTree()
    tree1.root = node1
    # adding the nodes to the tree :
    node1.add_node(node2, node3)
    node2.add_node(node4, node5)
    node4.add_node(node7, node8)
    node8.add_node(node11, node12)
    node11.add_node(node15)
    node3.add_node(node6)
    node6.add_node(node9, node10)
    node9.add_node(node13, node14)
    # displaying the tree from node 1 to the end on one line :
    print(node1.display_node(), "\n")
    # displaying the tree from the left to the right :
    print("_______________________________________________________________________")
    print(tree1.tree_left_right(),"\n")
    # displaying the tree from up to down :
    print("_______________________________________________________________________")
    print(tree1.tree_up_down(), "\n")
    # And adding it to a file :
    with open("the_tree.txt", "w", encoding = "utf-8") as tree_file :
        tree_file.write("Tree displayed from left to right :\n\n")
        tree_file.write(tree1.tree_left_right())
        tree_file.write("\n\n\n")
        tree_file.write("Tree displayed from up to down :\n\n")
        tree_file.write(tree1.tree_up_down())
    # to print the max_depth of the tree :
    print("The max depth of the tree is : ", tree1.tree_depth(), "\n")
    # to print the size of the tree :
    print("The size of the tree is : ", tree1.tree_size(), "\n")
