class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_redundant_vertices(self):
        redundant_vertices = [v for v in self.graph if len(self.graph[v]) == 2]

        for v in redundant_vertices:
            neighbors = self.graph[v]
            if len(neighbors) == 2:
                u, w = neighbors
                # Удаляем вершину v из списка соседей вершин u и w
                self.graph[u].remove(v)
                self.graph[w].remove(v)
                # Добавляем ребро между вершинами u и w, если его еще нет
                if w not in self.graph[u]:
                    self.graph[u].append(w)
                if u not in self.graph[w]:
                    self.graph[w].append(u)
                # Удаляем вершину v из графа
                del self.graph[v]

    def print_graph(self):
        for v in self.graph:
            print(f"{v}: {', '.join(map(str, self.graph[v]))}")


# Пример использования
g = Graph()

file = open('graph1.txt')

n = file.read(1)
print(n)
a = []
for i in file:
    for j in i:
        if j != " ":
            a.append(j)
print(a)
for i in range(0, int(n)*2, 2):
    print(a[i], a[i+1], sep='')
    g.add_edge(int(a[i]), int(a[i+1]))

print("Исходный граф:")
g.print_graph()

g.remove_redundant_vertices()

print("\nГраф после удаления избыточных вершин:")
g.print_graph()
