# An example of creating basic directed graphs in Python

class Graph:

    def __init__(self, name, vertices, edges):
        self.name = name
        self.vertices = vertices
        self.edges = edges

    def summary(self):
        print(f'Name: {self.name}\nVertices: {len(self.vertices)}' +
              f'\nEdges: {len(self.edges)}')


class Vertex:

    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


def find_vertex(name, vertices):
    for v in vertices:
        if name == v.name:
            return v
    return None


class Edge:
    def __init__(self, source, target, weight=0):
        self.source = source
        self.target = target
        self.weight = weight


def neighbors(vertex, graph):
    return [e.target for e in graph.edges if (e.source.name == vertex.name)]


def make_graph(name, vertices, edges):
    vertices = [v if (type(v) == list) else [v, 0] for v in vertices]
    vertices = [Vertex(x[0], x[1]) for x in vertices]
    edges = [e if (len(e) == 3) else [e[0], e[1], 0] for e in edges]
    edges = map(lambda e: [find_vertex(e[0], vertices),
                           find_vertex(e[1], vertices), e[2]], edges)
    edges = list(map(lambda e: Edge(e[0], e[1], e[2]), edges))
    return Graph(name, vertices, edges)


#---------------------------------------------------------------------------
# Examples
#---------------------------------------------------------------------------

# Example 1: Simple binary tree

N1 = 'Binary Tree'

V1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

E1 = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'],
      ['C', 'F'], ['C', 'G']]

#---------------------------------------------------------------------------
# End of File
#---------------------------------------------------------------------------
      
      
