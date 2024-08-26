from random import randint, choice
import numpy as np
from collections import deque


class MazeRunner:
    def __init__(self, m_hei, m_wid):
        self.maze = np.ones([m_hei, m_wid], dtype=int)
        k = [0, 0]
        if m_hei > 2 and m_wid > 2:
            k = [randint(1, m_hei - 2), randint(1, m_wid - 2)]
        self.frontier_cells = [k]
        self.m_hei = m_hei
        self.m_wid = m_wid
        self.m_entry = None
        self.m_exit = None
        self.path_found = False

    @staticmethod
    def print_space():
        print('  ', end='')

    @staticmethod
    def print_path():
        print('//', end='')

    @staticmethod
    def print_wall():
        print('\u2588\u2588', end='')

    def print_maze(self):
        for i in range(self.m_hei):
            for j in range(self.m_wid):
                if self.maze[i][j] == 1:
                    self.print_wall()
                else:
                    self.print_space()
            print('')
        print('\n\n')

    def print_maze_path(self):
        for i in range(self.m_hei):
            for j in range(self.m_wid):
                if self.maze[i][j] == 1:
                    self.print_wall()
                elif self.maze[i][j]:
                    self.print_path()
                else:
                    self.print_space()
            print('')
        print('\n\n')

    def find_next_cells(self, x, y, step):
        points = [[x, y - step], [x, y + step], [x + step, y], [x - step, y]]
        to_remove = []
        for p in points:
            if p[0] < 1 or p[0] > self.m_hei - 2:
                to_remove.append(p)
            elif p[1] < 1 or p[1] > self.m_wid - 2:
                to_remove.append(p)
        return [x for x in points if x not in to_remove]

    def add_between_cell(self, x, y):
        points = self.find_next_cells(x, y, 1)
        found = False
        for p in points:
            if found:
                break
            if self.maze[p[0]][p[1]] == 0:
                break
            neighbors = self.find_next_cells(p[0], p[1], 1)
            if [x, y] in neighbors:
                neighbors.remove([x, y])
            for n in neighbors:
                if self.maze[n[0]][n[1]] == 0:
                    found = True
                    self.maze[p[0]][p[1]] = 0
                    break

    def add_entry_and_exit(self):
        a_entry, a_exit = False, False
        for i in range(1, self.m_hei):
            if self.maze[i][1] == 0:
                self.maze[i][0] = 0
                a_entry = True
                break
        if not a_entry and self.m_wid > 2:
            for i in range(1, self.m_hei):
                if self.maze[i][2] == 0:
                    self.maze[i][0] = 0
                    self.maze[i][1] = 0
                    break
        for i in range(self.m_hei - 1, 1, -1):
            if self.maze[i][self.m_wid - 2] == 0:
                self.maze[i][self.m_wid - 1] = 0
                a_exit = True
                break
        if not a_exit and self.m_wid > 2:
            for i in range(self.m_hei - 1, 1, -1):
                if self.maze[i][self.m_wid - 3] == 0:
                    self.maze[i][self.m_wid - 2] = 0
                    self.maze[i][self.m_wid - 1] = 0
                    break

    def make_maze(self):
        while self.frontier_cells:
            p = choice(self.frontier_cells)
            self.maze[p[0]][p[1]] = 0
            self.add_between_cell(p[0], p[1])
            for point in self.find_next_cells(p[0], p[1], 2):
                if self.maze[point[0]][point[1]] != 0:
                    self.frontier_cells.append(point)
            self.frontier_cells.remove(p)
        self.add_entry_and_exit()

    def find_entry(self):
        for i in range(1, self.m_hei - 1):
            if not self.maze[i][0]:
                return [i, 0]
        return None

    def find_exit(self):
        for i in range(1, self.m_hei - 1):
            if not self.maze[i][self.m_wid - 1]:
                return [i, self.m_wid - 1]
        return None

    def is_exit(self, n):
        return self.m_exit == [n[0], n[1]]

    def find_neighbors(self, x):
        my_list = [[x[0], x[1] + 1], [x[0], x[1] - 1], [x[0] + 1, x[1]], [x[0] - 1, x[1]]]
        to_remove = []
        for n in my_list:
            if n[0] < 0 or n[0] >= self.m_hei or n[1] < 0 or n[1] >= self.m_wid:
                to_remove.append(n)
            elif self.maze[n[0]][n[1]] != 0:
                to_remove.append(n)
        return [i for i in my_list if i not in to_remove]

    def find_escape(self):
        if not self.path_found:
            my_queue = deque()
            visited = dict()
            self.m_entry = self.find_entry()
            self.m_exit = self.find_exit()
            elem = None
            found = False
            if self.m_entry and self.m_exit:
                visited[(self.m_entry[0], self.m_entry[1])] = [None, None]
                my_queue.append(self.m_entry + [None, None])
                while my_queue:
                    elem = my_queue.popleft()
                    visited[(elem[0], elem[1])] = [elem[2], elem[3]]
                    if self.is_exit(elem):
                        found = True
                        break
                    for neighbor in self.find_neighbors(elem):
                        if (neighbor[0], neighbor[1]) not in visited:
                            my_queue.append(neighbor + [elem[0], elem[1]])
                if found:
                    self.maze[elem[0]][elem[1]] = 2  # path is marked by twos
                    self.maze[elem[2]][elem[3]] = 2
                    elem = visited[(elem[2], elem[3])]
                    while elem[0]:
                        self.maze[elem[0]][elem[1]] = 2
                        elem = visited[(elem[0], elem[1])]
        self.print_maze_path()

