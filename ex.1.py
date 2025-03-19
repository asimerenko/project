from collections import deque

"""
Напишите программу, которая обходит граф в ширину и глубину. Граф
неориентированный, задаётся списками смежности и хранится в файле. Программа
должна вывести в консоль порядок посещения вершин при обходе в ширину и при
обходе в глубину. Проверьте работу вашей программы на следующих примерах:
1. полный граф из 4 вершин
2. дерево из 5 вершин
3. граф из 8 вершин с 2 компонентами связности   
"""  
# 1. полный граф из 4 вершин
# graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]] # cписок смежности, представляющий граф

# 2. дерево из 5 вершин
# graph = [[1, 2], [0], [0, 3, 4], [2], [2]]

# 3. граф из 8 вершин с 2 компонентами связности
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3], [6], [7, 8], [8], []]

start = 0 # начальная вершина для обхода

# обход в глубину   
def dfs(graph, start, visited):
    visited.append(start) 
    for to in graph[start]:
        if to not in visited:
            dfs(graph, to, visited)
    return visited
    

visited = []
n = 0
for i in range(len(graph)):
    if i not in visited:
        dfs(graph, i, visited)
        n += 1
print('Компонент связности в графе:', n)
print('Результат обхода в глубину:', visited)

# обход в ширину
def bfs(graph, start): 
    n = len(graph)
    q = deque([start])
    visited = [False] * n
    visited[start] = True
    order = [start] 

    while q:
        vertex = q.popleft() 
        for neighbor in graph[vertex]:
            if not visited[neighbor]: 
                visited[neighbor] = True
                q.append(neighbor) 
                order.append(neighbor)

    return order
result = bfs(graph, start)
print('Результат обхода в ширину:', result)  
