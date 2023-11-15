import heapq

def create_graph():
    graph = {}
    
    while True:
        edge = input("Введите ребро графа в формате 'A B 3' (или 'exit' для завершения): ").split()
        
        if edge[0].lower() == 'exit':
            break
        
        start_node, end_node, weight = edge
        weight = int(weight)
        
        # Добавляем ребро в граф
        if start_node in graph:
            graph[start_node][end_node] = weight
        else:
            graph[start_node] = {end_node: weight}
            
        # Добавляем обратное ребро (граф неориентированный)
        if end_node in graph:
            graph[end_node][start_node] = weight
        else:
            graph[end_node] = {start_node: weight}

    return graph

def dijkstra(graph, start):
    # Инициализация
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропуск, если найденное расстояние больше текущего
        if current_distance > distances[current_vertex]:
            continue

        # Обновление расстояний
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найденный путь короче
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример использования
graph = create_graph()
print("Ваш граф:")
print(graph, "\n")


start_vertex = input()
end_vertex = input()
result = dijkstra(graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex} до {end_vertex}: {result.get(end_vertex)}")
