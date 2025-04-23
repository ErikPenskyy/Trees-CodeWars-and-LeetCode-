def tree_by_levels(node: Node):
    """Sorts by nodes"""
    if node.value is None:
        return []
    list_of_trees = [node]
    list_of_nodes = []

    while True:
        for num, temp_tree in enumerate(list_of_trees):
            list_of_nodes.append(temp_tree.value)
            if temp_tree.left:
                list_of_trees.append(temp_tree.left)

            if temp_tree.right:
                list_of_trees.append(temp_tree.right)

            list_of_trees.pop(num)
            break

        if len(list_of_nodes) > 0 and not list_of_trees:
            break

    return list_of_nodes
