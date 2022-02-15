from collections import defaultdict
from dis import dis
from math import inf
import random
import csv
import numpy as np
from sklearn import datasets
from .sim import euclidean_dist


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    return np.mean(points, axis=1)


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    centers = []
    clusters = np.unique(assignments)

    for cluster_symbol in clusters:
        cluster_data = []
        for i in range(len(dataset)):
            if(assignments[i] == cluster_symbol):
                cluster_data.append(dataset[i])
        centroid = point_avg(cluster_data)
        centers.append(centroid)

    return np.array(centers)

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return euclidean_dist(a, b)

def distance_squared(a, b):
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return np.random.choice(dataset, k)

def cost_function(clustering):
    clusters = list(clustering)
    cost = 0
    for i in range(len(clusters)):
        cluster = clusters[i]
        dataset = clusters[cluster]
        for j in range(len(dataset)):
            cost += distance(cluster, dataset[i])

    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    pp = []
    for i in range(len(dataset)):
        point = dataset[i]
        c_point = 0
        for j in range(len(dataset)):
            dist = point - dataset[j]
            c_point += np.linalg.norm(dist)
        pp.append(dist)

    pp = (pp - np.min(pp)) / (np.min(pp) - np.max(pp))

    k_centroids = []
    for i in range(k):
        index = np.argmax(pp)
        k_centroids.append(dataset[index])
        pp[index] = np.min(pp)
    
    return k_centroids

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
