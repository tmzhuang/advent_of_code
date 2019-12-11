from .utils import run_prog

class Robot:
    def __init__(self, prog):
        self.prog = prog.copy()
        self.messages = deque()
        self.ip = 0
        self.last_output = None
        self.halted = False
        self.phase_set = False

    def __str__(self):
        return f'<Amp {self.name} - {self.phase}: IP:{self.ip}, output: {self.last_output}>'


    def __repr__(self):
        return str(self)

    def run(self, input_):
        result = run_prog(self.ip, self.prog, phase=self.phase, input_=input_, phase_set=self.phase_set)
        if result is None:
            self.halted = True
        else:
            self.last_output, self.ip, self.phase_set = result
        return self.last_output
