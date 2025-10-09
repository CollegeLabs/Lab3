from src.TreasureMapEnv import *
from src.graphClass import *

class TreasureMapGraph(Graph):
    def __init__(self, graph_dict=None):
      self.graph_dict = graph_dict or {}
      self.make_graph()

    def make_graph(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect(b, a, dist)

    def connect(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    def Map(Data):
      map = Graph(Data)

      net = Network(heading="Lab3. Treasure Map",
                bgcolor ="#242020",
                font_color = "white",
                height = "750px",
                width = "100%")   # do this
    
      net.add_nodes(map.nodes(), title=[str(node) for node in map.nodes()])

      nodeColors={
      "start":"red",
      "goal": "green",
      "frontier": "orange",
      "expanded":"pink",
      "Treasure":"yellow"
      }

      for node in net.nodes:
          if node['id']=='Room1':
              node["color"]=nodeColors["start"]
          elif node['id']=='Room48':
              node["color"]=nodeColors["goal"]

      edges=[]
      edges_labels=[]

      for node_source in map.nodes():
          for node_target, dist in map.get(node_source).items():
              if set((node_source,node_target)) not in edges:
                  net.add_edge(node_source,node_target, label=str(dist))
                  edges.append(set((node_source,node_target)))
                  edges_labels.append(str(dist))

      #net.show("graph1.html", notebook=False)
