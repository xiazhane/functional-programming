class Graph:
    def __init__(self):
        self.graph = {}
#Бұл класс бағытталмаған графикті білдіреді.
 # График іргелес тізім арқылы жүзеге асырылады, мұнда әрбір шың сөздіктің self.graph кілті болып табылады,
 # ал сәйкес мән көршілер тізімі болып табылады.
    def add_edge(self, vertex, neighbor):
        if vertex not in self.graph:

            self.graph[vertex] = []
        self.graph[vertex].append(neighbor)
        #Бұл әдіс іргелес тізімді жаңарту арқылы графикке жиекті қосады.
#Егер шыңы графикте әлдеқашан болмаса, ол сол кілттің мәні ретінде бос тізімді қосады.
#Содан кейін ол көршіні берілген шың үшін көршілер тізіміне қосады.

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()

        print(start_vertex, end=" ")
        visited.add(start_vertex)

        for neighbor in self.graph.get(start_vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Бұл әдіс берілген бастапқы_төбеден бастап Тереңдік-Бірінші Іздеу өтуін орындайды.
# Ол араланған шыңдарды бақылайтын жиын болып табылатын қосымша параметрді қажет етеді.
# Егер кірген жоқ болса, ол бос жиын ретінде инициализацияланады.
# Әдіс ағымдағы шыңды (start_vertex) басып шығарады және оны барған шыңдар жиынына қосады.
# Содан кейін ол ағымдағы шыңның әрбір кірмеген көршісі үшін dfs әдісін рекурсивті түрде шақырады.
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

# Graph класының данасы (g) жасалады және үлгі диаграмманы құру үшін оған жиектер қосылады.
print("DFS traversal starting from vertex 1:")
g.dfs(1)
