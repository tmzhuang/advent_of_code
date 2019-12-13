from collections import deque

import numpy as np

from .utils import run_prog

class Arcade:
    def __init__(self, prog):
        self.ip = 0
        self.prog = prog.copy()
        self.messages = deque()

    def __str__(self):
        return f'<Arcade: {self.messages}'

    def __repr__(self):
        return str(self)

    def read(self):
        self.update_map()
        color = self.map[self.position[0], self.position[1]]
        # print(f'Sending current color: {color}')
        return color

    def write(self, item):
        self.messages.append(item)

    def run(self, ip=self.ip, out=self):
        return run_prog(self.prog, ip=ip)
