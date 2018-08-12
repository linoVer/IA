# Variable Declarations
map_maze = {
    'A': [('B', 5)],
    'B': [('A', 5), ('C', 7), ('F', 2)],
    'C': [('B', 7), ('L', 8)],
    'D': [('E', 3)],
    'E': [('D', 3), ('I', 6)],
    'F': [('B', 2), ('G', 5), ('J', 6)],
    'G': [('F', 5), ('K', 6)],
    'H': [('I', 3)],
    'I': [('E', 6), ('J', 2)],
    'J': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
    'K': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
    'L': [('C', 8), ('K', 2), ('U', 9)],
    'M': [('N', 3)],
    'N': [('M', 3), ('O', 2), ('R', 7)],
    'O': [('J', 2), ('N', 2), ('P', 3)],
    'P': [('O', 3), ('S', 7)],
    'Q': [('R', 3)],
    'R': [('N', 7), ('Q', 3), ('S', 5)],
    'S': [('P', 7), ('R', 5), ('T', 2)],
    'T': [('K', 9), ('S', 2), ('U', 2)],
    'U': [('L', 9), ('T', 2)]
}

first_state = 'A'
objective_state = 'Q'

visited = [first_state]
result = [first_state]
state_ = first_state

less_state = ''
less_value = float('Inf')

count_cost = 0
boarder = [([first_state], 0)]

# Function declaration


def get_adjacent_not_visited(state_):
    global visited
    global map_maze

    states = map_maze[state_]
    return_ = []

    for s in states:
        if s[0] not in visited:
            return_.append(s)

    return return_


# Code Implementation


while state_ != objective_state:

    boarder = sorted(boarder, key=lambda x: x[1])
    path = boarder[0][0]
    cost = boarder[0][1]
    aux = path
    state_ = path[-1]

    not_visited = get_adjacent_not_visited(state_)

    if state_ != objective_state:
        del(boarder[0])
        if len(not_visited) != 0:
            for adj in not_visited:
                less_value = adj[1]
                less_state = adj[0]
                visited.append(less_state)
                path = [x for x in aux]
                path.append(less_state)
                count_cost = cost + less_value
                way = (path, count_cost)
                boarder.append(way)
    else:
        continue

result = boarder[0][0]
count_cost = boarder[0][1]


print("Caminho resultante: %s" % result)
print("Custo do caminho: %s" % count_cost)

