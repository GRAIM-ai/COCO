# graph adjacency_matrix
class Graph:
    def __init__(self, size):
        self.adj_list = [[0 for _ in range(size)] for i in range(size)]
        self.size = size

    def insert_edge(self, u, v):
        '''
        complete your code

        '''
        self.adj_list[u][v]=1
        self.adj_list[v][u]=1


    def display(self):
        for i in range(self.size):
            print_list = [i]
            for j in range(self.size):
                if self.adj_list[i][j] == 1:
                    print_list.append(j)
            if len(print_list) == 1:
                print(i)
            else:
                for j in range(len(print_list)):
                    if j != len(print_list) - 1:
                        print(print_list[j], end='->')
                    else:
                        print(print_list[j])


def main():
    graph = Graph(8)
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 3)
    graph.insert_edge(1, 4)
    graph.insert_edge(1, 5)
    graph.insert_edge(3, 6)
    graph.insert_edge(3, 7)

    graph.display()


'''
[output]

0->1->2->3
1->0->4->5
2->0
3->0->6->7
4->1
5->1
6->3
7->3

'''

main()