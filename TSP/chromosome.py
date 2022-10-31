# Reference: https://github.com/emre-kocyigit/genetic_algorithm_tsp/blob/main/Chromosome.py

# importing the libraries needed
import math

# getting the training dataset
FILE_NAME = 'genetic-algorithms-problems\TSP\data.txt'
DATASET = []

class Node(): 
    def __init__(self, id, x, y):
        """Generates the Location / coordinates / Point

        Args:
            id (str): ID feature
            x (float): X axis
            y (float): Y axis
        """
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)
    
# opening the training dataset
with open(FILE_NAME, 'r') as f:
    for line in f:
        # removing the empty spaces
        line = line.strip()
        # splitting 
        items = line.split(' ')
        id, x, y = items[0], items[1], items[2]
        # creating the NODE object
        DATASET.append(Node(id = id, x = x, y = y))

# getting the size of dataset. Total number of points. 
N = len(DATASET) + 1 # adding 1 for including the starting point

def create_distance_matrix(node_list):
    """Creating a EUCLIDEAN distance matrix for distance

    Args:
        node_list (NODE): Node Object which we created before

    Returns:
        _type_: _description_
    """
    
    # creating a matrix with all 0s in it
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    
    # calculating the EUCLIDEAN distance between each and every points 
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[0]) - 1):
            # getting that particular element in the matrix and calculating the euclidean distance
            matrix[node_list[i].id][node_list[j].id] = math.sqrt(pow((node_list[i].x - node_list[j].x), 2)
                                                                + pow((node_list[i].y - node_list[j].y), 2))
    return matrix

# distance_matrix = create_distance_matrix(node_list = DATASET)
# print(len(distance_matrix))

# TODO:
# Need to understand why 0 index in the matrix is having all 0s instead of distances between them.
# print(distance_matrix)

class Chromosome:
    def __init__(self, node_list):

        # TODO:
        # Need to understand this function properly

        # This chromosome is used for cross over, mutation and other operations
        self.chromosome = node_list
        # to explain route in a simple clear way
        chromosome_representation = []
        for i in range(0, len(node_list)):
            chromosome_representation.append(self.chromosome[i].id)
        self.chromosome_representation = chromosome_representation
        print(len(chromosome_representation))
        
        distance = 0
        distance_matrix = create_distance_matrix(node_list = DATASET)
        # getting distances from the matrix
        for i in range(1, len(self.chromosome_representation) - 1):
            distance += distance_matrix[self.chromosome_representation[i] - 1][self.chromosome_representation[i + 1] - 1]
        self.cost = distance
        self.fitness_value = 1 / self.cost
            
# Chromosome(DATASET)