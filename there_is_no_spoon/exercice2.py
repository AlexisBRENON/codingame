import sys, math

# Don't let the machines win. You are humanity's last hope...
NONE_NODE =     {
                    'coord': (-1, -1),
                    'expected': -1,
                    'current': 0,
                    'links' : {
                        'top' : 0,
                        'right' : 0,
                        'bottom': 0,
                        'left': 0
                    }
                }
OPPOSITE = {
    'left': 'right',
    'right' : 'left',
    'top' : 'bottom',
    'bottom' : 'top'
    }

def log(string):
    sys.stderr.write(string + "\n")

width = int(input()) # the number of cells on the X axis
height = int(input()) # the number of cells on the Y axis
grid = []


j = 0
for y in range(height):
    grid.append([])
    line = input() # width characters, each either 0 or .
    i = 0;
    for c in line:
        if c != '.' :
            grid[j].append(
                {
                    'coord': (i, j),
                    'expected': int(c),
                    'current': 0,
                    'links' : {
                        'top' : 0,
                        'right' : 0,
                        'bottom': 0,
                        'left': 0
                    }
                })
        else:
            grid[j].append(NONE_NODE)
        i += 1
    j += 1

def get_right(x, y):
    x = x+1
    while (x < len(grid[y])):
        if (grid[y][x]['coord'] != (-1, -1)):
            return grid[y][x]
        else:
            x += 1
    return NONE_NODE

def get_left(x, y):
    x = x-1
    while (x >= 0):
        if (grid[y][x]['coord'] != (-1, -1)):
            return grid[y][x]
        else:
            x -= 1
    return NONE_NODE


def get_bottom(x, y):
    y = y+1
    while (y < len(grid)):
        if (grid[y][x]['coord'] != (-1, -1)):
            return grid[y][x]
        else:
            y += 1
    return NONE_NODE   

def get_top(x, y):
    y = y-1
    while (y >= 0):
        if (grid[y][x]['coord'] != (-1, -1)):
            return grid[y][x]
        else:
            y -= 1
    return NONE_NODE

def create_links(current_node):
    result = ""
    if current_node['expected'] > current_node['current']:
        log("Creating links from : " + str(current_node['coord']))
        left = get_left(*current_node['coord'])
        top = get_top(*current_node['coord'])
        right = get_right(*current_node['coord'])
        bottom = get_bottom(*current_node['coord'])
        priority_list = [(left, 'left'), (top, 'top'), (right, 'right'), (bottom, 'bottom')]
        priority_list = [ node for node in priority_list if node[0]['coord'] != (-1, -1) and node[0]['expected'] - node[0]['current'] > 0]
        priority_list.sort(key=lambda node: node[0]['expected'] - node[0]['current'], reverse=True)
        
        max_links = 0
        for node in priority_list:
            result += add_links(current_node, node, math.floor((current_node['expected']-current_node['current'])/len(priority_list)))
    return result
    
def add_links(from_node, to_node, max_links):
    result = ""
    while from_node['current'] < from_node['expected'] and from_node['links'][to_node[1]] < 2 and to_node[0]['current'] < to_node[0]['expected'] and max_links > 0:
        max_links -= 1
        create_link(from_node, to_node[1], to_node[0])
    return result

def create_link(from_node, direction, to_node):
    from_node['current'] += 1
    from_node['links'][direction] += 1
    to_node['current'] += 1
    to_node['links'][OPPOSITE[direction]] += 1
    result = "{} {} {} {} 1".format(from_node['coord'][0], from_node['coord'][1], to_node['coord'][0], to_node['coord'][1])
    log(result)
    print(result)
    

n = 8
while n >= 1:
    j = 0
    for y in grid:
        i = 0
        for x in y:
            if x['expected'] >= n:
                create_links(x)
            i += 1
        j += 1
    n -= 1
