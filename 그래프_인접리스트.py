# graph adjacency_list

class Vertex:
    def __init__(self, item):
        self.value = item
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
    def add_last(self, item):
        temp = self.head
        if temp == None:
            self.head = Vertex(item)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Vertex(item)


class Graph:
    def __init__(self, size):
        self.adj_list = [None] * size
        self.size = size

    def insert_edge(self, u, v):
        if self.adj_list[u] == None:
            lk = linkedlist()
            self.adj_list[u] = lk
            '''
            complete your code

            '''
            self.adj_list[u].head=Vertex(u)
            self.adj_list[u].add_last(v)
        else:
            '''
            complete your code

            '''
            self.adj_list[u].add_last(v)

        if self.adj_list[v] == None:
            self.adj_list[v] = linkedlist()
            '''
            complete your code

            '''
            self.adj_list[v].head = Vertex(v)
            self.adj_list[v].add_last(u)
        else:
            '''
            complete your code

            '''
            self.adj_list[v].add_last(u)
    def display(self):
        for i in range(self.size):
            if self.adj_list[i] == None:
                continue
            temp = self.adj_list[i].head

            while temp != None:
                if temp.next == None:
                    print(temp.value)
                    break
                else:
                    print(temp.value, end='->')
                temp = temp.next
        print()


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


main()

'''
[[output]]

0->1->2->3
1->0->4->5
2->0
3->0->6->7
4->1
5->1
6->3
7->3

'''