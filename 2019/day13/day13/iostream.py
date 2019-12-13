from collections import deque
class IOStream:
    def __init__(self, in_=None, out=None, arr=[]):
        self.in_ = in_
        self.out = out
        self._buffer = deque(arr)

    def write(self, item):
        if self.out == 'stdout':
            print(item)
        else:
            return item

    def read(self):
        try:
            item = self._buffer.popleft()
        except IndexError:
            item = None
        if self.in_ == 'stdin':
            return int(input('Input: '))
        else:
            self._buffer.append(item)
