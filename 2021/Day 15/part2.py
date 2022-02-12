import numpy as np
import sys
import part1
import matplotlib.pyplot as plt
import time
from queue import PriorityQueue

np.set_printoptions(threshold=sys.maxsize)

def create_graph(risk_levels):

    graph = {}
    attributes = ['Position', 'Neighbours', 'Score', 'H-Score', 'Visited']

    for i in range(risk_levels.shape[0]):
        for j in range(risk_levels.shape[1]):
            attr = dict.fromkeys(attributes)
            # Determine neighbours
            neighbours = []
            if not i == 0:
                neighbours.append((i-1, j))
            if not j == 0:
                neighbours.append((i, j-1))
            if not i == risk_levels.shape[0] - 1:
                neighbours.append((i+1 , j))
            if not j == risk_levels.shape[1] - 1:
                neighbours.append((i, j+1))

            id = max(i * risk_levels.shape[1] + j, 0)

            attr['id'] = id
            attr['Position'] = (i, j)
            attr['Neighbours'] = neighbours
            attr['Score'] = np.inf
            attr['H-Score'] = np.inf
            attr['Visited'] = False 
            attr['Antecedent'] = None
            attr['Risk'] = risk_levels[i][j]
      
            graph[(i, j)] = attr
            attr = {}

    return graph

def build_path(targetNode):

    score = 0
    route = []
    currentNode = targetNode
    while currentNode: 
        route.append(currentNode['Position'])
        if not currentNode['Position'] == (0, 0): score += int(currentNode['Risk'])
        currentNode = currentNode['Antecedent']
  
    return route, score


def get_node_with_lowest_score(graph, risk_levels, queue):

    while True:
        node = queue.get()[2]
        if node['Visited'] == False:
            return node


def manhattan_distance(nextNode, goalNode):

    x1, y1 = nextNode['Position']
    x2, y2 = goalNode['Position']
    distance = np.abs(x1 - x2) + np.abs(y1 - y2)

    return distance

def do_a_star(graph, start, goal, risk_levels):

    # Init starting node
    graph[start]['Score'] = 0
    graph[start]['H-Score'] = 0

    startNode = graph[start]
    targetNode = graph[goal]

    myQueue = PriorityQueue()
    myQueue.put((startNode['H-Score'], startNode['id'], startNode)) # Add first node to queue

    while True: # Run forever until return statement reached

        start = time.time()

        currentNode = get_node_with_lowest_score(graph, risk_levels, myQueue)
        end = time.time()

        currentNode['Visited'] = True
        # print(f"Node position: {currentNode['Position']}. Time taken {round(end - start, 4)}s")

        for nextNode in currentNode['Neighbours']:
            nextNode = graph[nextNode]
            if nextNode['Visited'] == False: # Update subsequent nodes, add to priority queue
                i, j = nextNode['Position']
                newScore = currentNode['Score'] + int(risk_levels[i][j])
                if newScore < nextNode['Score']:
                    nextNode['Score'] = newScore
                    nextNode['H-Score'] = newScore + manhattan_distance(nextNode, targetNode)
                    nextNode['Antecedent'] = currentNode

                myQueue.put((nextNode['H-Score'], nextNode['id'], nextNode))

        if currentNode == targetNode:
            return build_path(targetNode)


def increment(x, n, k):
    y = int(x) + n + k
    if y > 9: y = y - 9
    return y

def unfold_map(risk_levels):

    rows = []
    for k in range(5):
        cols = []
        for n in range(5):

            cols.append(np.array([[increment(x, n, k) for x in row] for row in risk_levels]))

        rows.append(np.concatenate(np.array(cols), axis=1))
    new_map = np.concatenate(np.array(rows), axis=0)

    return new_map

def main():

    risk_levels = part1.import_file()
    entire_risk_levels = unfold_map(risk_levels)

    target_position = (entire_risk_levels.shape[0]-1, entire_risk_levels.shape[1]-1)
    graph = create_graph(entire_risk_levels)

    starting_position = (0, 0)
    target_position = list(graph.keys())[-1]

    _, score = do_a_star(graph, starting_position, target_position, entire_risk_levels)
    print(score)

if __name__ == '__main__':
    main()