import sys, math
tree = {
    'nodes': {},
    'degrees': {
        0: {}
    }
}
longest_path = 0
max_degree = 0


n = int(input()) # the number of adjacency relations
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    
    if xi not in tree['nodes']:
        tree['nodes'][xi] = {'distances' : {}}
        tree['degrees'][0][xi] = True
        longest_path = longest_path + 1
    if yi not in tree['nodes']:
        tree['nodes'][yi] = {'distances' : {}}
        tree['degrees'][0][yi] = True
        longest_path = longest_path + 1
    
    xi_degree = len(tree['nodes'][xi]['distances'])
    yi_degree = len(tree['nodes'][yi]['distances'])
    del tree['degrees'][xi_degree][xi]
    del tree['degrees'][yi_degree][yi]
    tree['nodes'][xi]['distances'][yi] = 1
    tree['nodes'][yi]['distances'][xi] = 1
    if xi_degree + 1 not in tree['degrees']:
        tree['degrees'][xi_degree+1] = {}
    if yi_degree + 1 not in tree['degrees']:
        tree['degrees'][yi_degree+1] = {}
    tree['degrees'][xi_degree+1][xi] = True
    tree['degrees'][yi_degree+1][yi] = True


def debug():
    sys.stderr.write("{\n")
    for node_idx, node in tree['nodes'].items():
        sys.stderr.write(str(node_idx) + ": { ")
        for distant_node, distance in node['distances'].items():
            sys.stderr.write(str(distant_node) + "(" + str(distance) + ") ")
        sys.stderr.write("}\n")
    sys.stderr.write("}\n")

outtermost_nodes = tree['degrees'][1].keys()
longest_path = 0
while len(outtermost_nodes) > 1:
    debug()
    longest_path += 1
    new_outtermost = []
    for node_idx in outtermost_nodes:
        if len(tree['nodes'][node_idx]['distances']) == 1:
            neighbor = list(tree['nodes'][node_idx]['distances'].keys())[0]
            print("Moving from %s to %s" % (node_idx, neighbor), file=sys.stderr)
            new_outtermost.append(neighbor)
            del tree['nodes'][node_idx]
            del tree['nodes'][neighbor]['distances'][node_idx]
    outtermost_nodes = list(set(new_outtermost))

print(longest_path)

