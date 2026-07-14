import networkx as nx


class MST:

    def calculate(self, graph):

        mst = nx.minimum_spanning_tree(
            graph,
            weight="length",
        )

        return mst