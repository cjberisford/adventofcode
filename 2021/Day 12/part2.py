def import_file():
    with open('input/example.txt') as f:
        transitions = f.read().split('\n')
    transitions_pairs = [tuple(line.split('-')) for line in transitions]

    return transitions_pairs

def get_transition_model(transition_pairs):
    transitions = {}
    unique_nodes = set(list(sum(transition_pairs, ())))
    for node in list(unique_nodes):
        transitions[node] = [x[1] for x in transition_pairs if x[0]==node]

    return transitions

def pathfinder(transitions, successors, antecedents, current_node, paths, visited):

    successors = transitions[current_node]

    # Add node to path history
    antecedents.append(current_node)
    if current_node.islower():
        visited.append(current_node)

    # print(f"Pathfinder is located at {current_node} with possible transitions to {successors}. Current path is {antecedents}")
    for successor in successors:
        if successor == 'end' and antecedents + ['end'] not in paths:
            antecedents.append('end')
            path = antecedents
            return path
        elif successor == 'end':
            pass
            # print("This path has previously been found, returning to parent node")

        if successor not in visited and successor != 'end':
            # print("Branching")
            path = pathfinder(transitions, successors, antecedents, successor, paths, visited)
            if path:
                return path

    # Node unused to delete from pathing history -- MUST be the LAST element
    antecedents.pop()
    if current_node.islower():
        visited.remove(current_node)

 
def explore(transitions):

    paths = []

    while None not in paths:
        antecedents = []
        visited = []
        successors = transitions['start']
        path = pathfinder(transitions, successors, antecedents, 'start', paths, visited)
        paths.append(path)

    for path in paths[:-1]:
        print(path)

    print(len(paths[:-1]))

    
def main():
    transition_pairs = import_file()
    inverse_pairs = [(sub[1], sub[0]) for sub in transition_pairs]
    transitions = get_transition_model(transition_pairs)
    inverse_transitions = get_transition_model(inverse_pairs)

    # Concatenate dicts
    for key in transitions.keys():
        transitions[key] += inverse_transitions[key]

    explore(transitions)


if __name__ == '__main__':
    main()