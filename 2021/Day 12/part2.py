from collections import Counter
import random

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

def get_prohibited_transitions(successors, antecedents):

    # Count occurrences of small caves
    small_caves = [x for x in antecedents if x.islower()]
    small_cave_count = Counter(small_caves)
    max_visits = small_cave_count.most_common()

    # Compile list of prohibited locations
    prohibited_transitions = []
    for node in antecedents:
        if small_cave_count[node] >= 1 and max_visits[0][1] >= 2:
            prohibited_transitions.append(node)
    
    prohibited_transitions.append('start')
    prohibited_transitions.append('end')

    return prohibited_transitions


def pathfinder(transitions, successors, antecedents, current_node, paths):

    print(antecedents)

    # Get list of possible transitions from current state
    successors = transitions[current_node]
    
    # Add node to path history
    antecedents.append(current_node)

    for successor in successors:

        # Scan antecedents for small caves, creating a list of nodes that can't be visited dynamically
        invalid_transitions = get_prohibited_transitions(successors, antecedents)

        # # Try shuffling order of successors -- Might help, who knows?
        # random.shuffle(successors)

        if successor == 'end' and antecedents + ['end'] not in paths:
            # New path found, add it to paths and keep looking for more routes
            print("FOUND PATH, adding...")
            antecedents.append('end')
            path = antecedents
            # paths.append(path)
            return path
        elif successor == 'end':
            pass
            # print("This path has previously been found, returning to parent node")

        if successor not in invalid_transitions:
            path = pathfinder(transitions, successors, antecedents, successor, paths)
            if path:
                return path

    # Node unused to delete from pathing history -- MUST be the LAST element
    antecedents.pop()
 
def explore(transitions):

    paths = []
    starting_node = 'start'
    antecedents = []
    successors = transitions['start']


    while None not in paths:
        antecedents = []
        print("STARTING PATHFINDER")
        path = pathfinder(transitions, successors, antecedents, starting_node, paths)
        print("TERMINATING FUNCTION CALL, FOUND A PATH!", path)
        print(" ")
        paths.append(path)

    for path in paths[:-1]:
        print(path)
    print("Paths found:", len(paths[:-1]))

    
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