import numpy as np
import typing


class AdjacencyList(object):

    @staticmethod
    def count_vertices_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int: #dictionary(key, values) -> dictionary(vertices, edges)
        """
        Counts the number of vertices in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of vertices
        """

        number_of_vertices = len(adj_list.keys())
        return number_of_vertices

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_edges_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of edges
        """
        
        edges=0
        for vertice in adj_list.values(): 
            edges+=len(vertice)

        edges = edges/2
        return edges

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_vertices_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of vertices in a directed graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of vertices
        """
        
        number_of_vertices = len(adj_list.keys())
        print(number_of_vertices)
        return number_of_vertices


        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_edges_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of nodes/vertices
        """
        
        edges=0
        for vertice in adj_list.values(): 
            edges+=len(vertice)

        return edges

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def count_odd_neighbours_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of vertices that have an odd number of neighbours

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of edges
        """
        
        odd_neighbours = 0
        for key in adj_list.keys():
            edges = adj_list.get(key)
            if len(edges)%2==1: odd_neighbours+=1

        return odd_neighbours

        raise NotImplementedError('Function not implemented yet')

    @staticmethod
    def list_to_matrix(
            adj_list: typing.Dict[int, typing.List[int]]) -> np.array:
        """
        Accepts a graph in the adjacency list format, and returns it in the
        adjacency matrix format.

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        """

        #nxn zeros array
        #
        #
        matrixlength=len(adj_list.keys())
        adjacentarray = np.zeros((matrixlength, matrixlength))
        for key in adj_list.keys():
            edges = adj_list.get(key)
            adjacentarray[key,edges]=1
            adjacentarray[edges,key]=1

        return adjacentarray

        raise NotImplementedError('Function not implemented yet')
