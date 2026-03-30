from collections import deque

def hasNumbers(inputString):
    return inputString.isnumeric()

def search(name, graph):
    search_queue = deque()
    search_queue += graph[name]

    searched = set()
    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if hasNumbers(person):ki
                return True
            else:
                searched.add(person)
                search_queue += graph[person]

    return False


graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'a'],
    'd':[],
    'e':['1'],
    'f':['a'],
}

print(search('a', graph))