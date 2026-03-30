import os
from collections import deque

'''
def printDir(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)

    searched = set()
    while search_queue:
        cur_dir = search_queue.popleft()

        for files in sorted(os.listdir(cur_dir)):
            full_path = os.path.join(cur_dir, files)
            if os.path.isfile(full_path) and full_path not in searched:
                print(f'{cur_dir}: {files}')
                searched.add(full_path)
            else:
                search_queue.append(full_path)
'''
# Поиск в ширину
def wideSearch(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        cur_dir = search_queue.popleft()

        for files in sorted(os.listdir(cur_dir)):
            full_path = os.path.join(cur_dir, files)
            if os.path.isfile(full_path) and str(files) == "1.txt":
                print(f'Нашёл! {cur_dir}: {files}')
                return True
            else:
                search_queue.append(full_path)

    return False

# Поиск в глубину
flag = False    # чуток костыль
def deepSearch(start_dir):
    global flag
    for files in sorted(os.listdir(start_dir)):
        full_path = os.path.join(start_dir, files)
        if os.path.isfile(full_path) and str(files) == "1.txt":
            print(f'Нашёл! {start_dir}: {files}')
            flag = True
            return True

        elif os.path.isdir(full_path) and not flag:
            deepSearch(full_path)

print('Поиск в ширину:')
wideSearch('C:\\Games\\test')

print('Поиск в глубину:')
deepSearch('C:\\Games\\test')