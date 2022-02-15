from .sim import euclidean_dist
import matplotlib.pyplot as plt
import numpy as np
class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon

    def snapshot(self, P_index, assignments):
        fig, ax = plt.subplots()
        colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
        colors = np.hstack([colors] * 20)
        circle1 = plt.Circle((self.dataset[P_index][0], self.dataset[P_index][1]), self.epsilon, color='r', fill = False)
        ax.add_patch(circle1)
        ax.scatter(self.dataset[:, 0], self.dataset[:, 1], color=colors[assignments].tolist(), s=10, alpha=0.8)
        # plt.show()
        fig.savefig("tmp.png")
        plt.close()

    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        
        assignments = [0 for _ in range(len(self.dataset))]
        cluster = 1

        for P_index in range(len(self.dataset)):

            if assignments[P_index] != 0:
                # already part of a cluster
                # skip
                continue

            if len(self.epsilon_neighborhood(P_index)) >= self.min_pts:
                # core point
                assignments = self.explore_and_assign_eps_neighborhood(
                    P_index, cluster, assignments
                )

            cluster += 1

        return assignments

    # helper function to find neighborhood given the index of point in dataset
    def epsilon_neighborhood(self, P_index):
        neighborhood = []
        
        for PN in range(len(self.dataset)):
            if PN != P_index and euclidean_dist(self.dataset[PN], self.dataset[P_index]) <= self.epsilon:
                # in the neighborhood
                neighborhood.append(PN)
        return neighborhood

    def explore_and_assign_eps_neighborhood(self, P_index, cluster, assignments):
        # get all neighbors
        neighborhood = self.epsilon_neighborhood(P_index)

        while neighborhood:
            # get the first neighbor in neighborhood
            neighbor_of_P = neighborhood.pop()
            
            if assignments[neighbor_of_P] != 0:
                # this point has already been assigned
                continue

            assignments[neighbor_of_P] = cluster
            self.snapshot(neighbor_of_P, assignments)
            # if neighbor_of_P is a core point, then should recursively 
            next_neighborhood = self.epsilon_neighborhood(neighbor_of_P)
            if len(next_neighborhood) >= self.min_pts:
                # this is a core point
                # its neighbors should be explored
                neighborhood.extend(next_neighborhood)

        return assignments
