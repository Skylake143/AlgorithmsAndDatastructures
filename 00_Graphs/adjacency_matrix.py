import numpy as np


class AdjacencyMatrix(object):

    @staticmethod
    def count_vertices_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices in an undirected graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices
        """
        count_vertices = np.size(adj_matrix[0])
        return count_vertices

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_edges_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of edges
        """
        vertices = np.where(adj_matrix!=0)
        edges = len(vertices[0])
        edges = int(edges/2)

        return edges
        

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_vertices_directed_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices in an directed graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices
        """

        count_vertices = np.size(adj_matrix[0])
        return count_vertices 

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_edges_directed_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of edges in an directed graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of edges
        """
        
        vertices = np.where(adj_matrix!=0)
        edges = len(vertices[0])

        return edges

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_odd_neighbours_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices that have an odd number of neighbours

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices that have an odd number of
        neighbours
        """
        odd_neighbours=0
        for row in adj_matrix: 
            if len(np.where(row!=0)[0])%2==1: odd_neighbours+=1
        return odd_neighbours

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def invert_directed_graph(adj_matrix: np.array) -> np.array:
        """
        Inverts the graph represented in adj_matrix in such a way, that each
        edge is switched direction, i.e., if there was an edge from
        adj_matrix[i][j] it will be directed the other way around, and vice
        versa. Pay additional attention to vertices that are connected in both
        directions.

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: numpy array, representing the inverted graph
        """
        
        transpose = np.transpose(adj_matrix)

        return transpose


        raise NotImplementedError('Function not implemented yet')
