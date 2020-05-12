""" https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/solutions/python """


def loop_size(node):
    node_list = []
    while hasattr(node, 'next') and node not in node_list:
        node_list.append(node)
        node = node.next
    index = node_list.index(node)
    new_node_list = node_list[index:]
    return len(new_node_list)


class Node:
    pass


nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
loop_size(nodes[0])



