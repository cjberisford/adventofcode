from collections import Counter
import random
import time
import itertools

def import_file():
    with open('input/example3.txt') as f:
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


def pathfinder(transitions, successors, antecedents, current_node, paths, closed_paths):


    successors = transitions[current_node] # Get list of possible transitions from current state
    antecedents.append(current_node) # Add node to current path
    invalid_transitions = get_prohibited_transitions(successors, antecedents) # Scan antecedents for small caves, creating a list of nodes that can't be visited dynamically

    for successor in successors:

        # Try shuffling order of successors -- Might help, who knows? 
        # It does as it encourages exploration, but it misses some solutions
        # random.shuffle(successors)

        if successor == 'end' and antecedents + ['end'] not in paths:
            # New path found, add it to paths and keep looking for more routes
            antecedents.append('end')
            path = antecedents
            return path, closed_paths # Exit function returning the path
    
        if successor not in invalid_transitions and antecedents + [successor] not in closed_paths:
            path, closed_paths = pathfinder(transitions, successors, antecedents, successor, paths, closed_paths)

            # successor_counter += 1
            if path:
                return path, closed_paths
            else:
                # At this point, close the node, but only if it has no successors
                closed_paths.append(antecedents + [successor])

    antecedents.pop() # Remove node from path as it has exited without finding any solutions

    return None, closed_paths

def explore(transitions):

    paths = []
    starting_node = 'start'
    antecedents = []
    successors = transitions['start']
    closed_paths = []
    path_number = 0

    while None not in paths:
        antecedents = []
        start_time = time.time() 
        path, closed_paths = pathfinder(transitions, successors, antecedents, starting_node, paths, closed_paths)
        print(f"Located path #{path_number} at {path}. Time taken {round(time.time() - start_time, 4)} seconds")
        paths.append(path)
        path_number += 1

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