Удаление избыточных вершин на графе.

Исходя из условия задачи, обозначим избычточными вершинами те вершины, имеющие ровно два ребра.

Программа включает в себя алгоритм удаления избыточных вершин на графе, что облегчает 
пользователю работу с приложением.

Описание алгоритма по удалению избыточных вершин:

1.Создаем список redundant_vertices, в котором будем хранить все избыточные вершины. Этот список инициализируется пустым.

2.Проходим по каждой вершине v в графе и проверяем её соседей. Если у вершины v количество соседей равно 2, то добавляем вершину v в список redundant_vertices.

3.Перебираем все вершины v в списке redundant_vertices.

4.Для каждой вершины v получаем список её соседей neighbors.

5.Если количество соседей neighbors равно 2, то получаем вершины u и w из списка neighbors.

6.Удаляем вершину v из списка соседей вершин u и w, вызывая метод remove для списка self.graph[u] и self.graph[w].

7.Проверяем, есть ли уже ребро между вершинами u и w. Если его нет, добавляем это ребро, вызывая метод append для списков self.graph[u] и self.graph[w].

8.Удаляем вершину v из графа, используя оператор del.

9.Печатаем граф после удаления избыточных вершин, вызывая метод print_graph.

Таким образом, данный метод проходит по всем вершинам графа, определяет избыточные вершины и удаляет их, а также обновляет связи между вершинами, чтобы сохранить 
связность графа. Он модифицирует исходный граф в соответствии с этими изменениями.

Как пользоваться:
В текстовый документ "graph1.txt" записываются данные о графе. 
Пример входных данных:

3 12 23 34 

Первое число - количество ребер. Остальные двухзначные числа - пара связных вершин 
неорентрированного графа. В данном примере ответом будет являтся граф 1-4, 4-1. 

Запустите файл "algo.py". Программа выведет получившийся граф. 

С уважением, команда разработчиков PoBedolagi.

Капитан: Дзензура Иван Михайлович

Участник: Парфиров Алесандр Владимирович
