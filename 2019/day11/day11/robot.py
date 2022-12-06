from collections import deque

import numpy as np

from .utils import run_prog

LEFT = 0
RIGHT = 1

UNDISCOVERED = '0'
WALL = '1'
PATH = '2'
ROBOT = '3'

PIXEL_MAPPING = {
        UNDISCOVERED: ' ',
        WALL = '#',
        PATH = '-',
        ROBOT = 'o'}


class Robot:
    def __init__(self, prog):
        self.ip = 0
        self.prog = prog.copy()
        self.messages = deque()
        self.direction = np.array((-1, 0))
        self.map = np.zeros((100,100), dtype=int)
        self.position = np.array((49,49))
        self.map[self.position[0], self.position[1]] = 1
        self.painted = []

    def __str__(self):
        return f'<Robot {self.position}, {self.direction}: {self.messages}'

    def __repr__(self):
        return str(self)

    def read(self):
        direction
        self.update_map()
        color = self.map[self.position[0], self.position[1]]
        # print(f'Sending current color: {color}')
        return color

    def update_map(self):
        if len(self.messages) != 2:
            # print(f'Ignoring update_map request: {self.messages}')
            return
        # print(f'Reading messages: {self.messages}')
        color = self.messages.popleft()
        new_direction = self.messages.popleft()
        self.paint(color)
        self.move(new_direction)

    def map_str(self):
        s = ''
        for row in self.map:
            row_str = ''.join(map(str, self.map))
            for pixel_str in PIXEL_MAPPING.keys():
                row_str = row_str.replace(pixel_str, PIXEL_MAPPING[pixel_str])
                s += row_str
                s += '\n'
        return s

    def move(self, direction):
        # print(f'Moving {direction} from {self.position}.')
        if direction == LEFT:
                self.direction[0], self.direction[1] = -self.direction[1], self.direction[0]
        elif direction == RIGHT:
            self.direction[0], self.direction[1] = self.direction[1], -self.direction[0]
        else:
            raise ValueError(f'Invalid direction {direction} provided.')
        self.position += self.direction
        # new_position = self.position +self.direction
        # if (np.all(new_position >= 0)
                # and np.all(new_position < 5)):
            # self.position = new_position
        # print(f'Moved {self.direction}. Now at {self.position}.')

    def write(self, item):
        self.messages.append(item)

    def run(self):
        return run_prog(self.prog, in_=self, out=self)

    def painted_count(self):
        return len(set(self.painted))
