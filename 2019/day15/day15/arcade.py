from collections import deque
import logging

import numpy as np

from .utils import run_prog

logger = logging.getLogger()

def get_char(val):
    charmap = {
            0: ' ',
            1: '#',
            2: '=',
            3: '_',
            4: 'o'}
    return charmap[val]


class Arcade:
    def __init__(self, prog):
        self.ip = 0
        self.prog = prog.copy()
        self.score = 0
        self.state = np.empty((21,39), dtype='<U1')
        self.messages = deque()
        self.last_input = 0
        self.ball_x = []
        self.paddle_x = None

    def __str__(self):
        return f'<Arcade: {self.messages}'

    def __repr__(self):
        return str(self)

    def read(self):
        self.update_state()
        print(f'{self.score=}')
        self.print_state()
        move = self.calculate_move()
        logger.debug(f'Sending move: {move}')
        return move

    def calculate_move(self):
        if len(self.ball_x) > 1:
            ball_dir = self.ball_x[-1] - self.ball_x[-2]
            if (ball_dir > 0) and (self.paddle_x < self.ball_x[-1]):
                return 1
            elif (ball_dir < 0) and (self.paddle_x > self.ball_x[-1]):
                return -1
        return 0

    def get_user_input(self):
        success = False
        while not success:
            try:
                raw = input(f'Enter move:')
                input_ = int(raw)
                success = input_ in [0, -1, 1]
            except:
                if not raw:
                    input_ = self.last_input
                    success = True
        self.last_input=input_
        return input_

    def update_state(self):
        n = len(self.messages)
        messages = np.array(self.messages).reshape((n//3, 3))
        for message in messages:
            x, y, val = message
            if x==-1 and y==0:
                self.score = val
            else:
                if val == 3:
                    self.paddle_x = x
                elif val == 4:
                    self.ball_x.append(x)
                self.state[y, x] = get_char(val)
        self.messages.clear()

    def print_state(self):
        logger.debug(f'{self.paddle_x=}')
        logger.debug(f'{self.ball_x=}')
        for line in self.state:
            print(''.join(line))
        print()

    def write(self, item):
        self.messages.append(item)

    def run(self, ip=None):
        if not ip:
            ip = self.ip
        run_prog(self.prog, ip=ip, out=self, in_=self)
        self.update_state()
        print(f'{self.score=}')
        self.print_state()
