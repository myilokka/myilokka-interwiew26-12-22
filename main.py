import random
import time
import uuid


class RandomSignal:

    def __init__(self):
        self.choice = [1, -1]
        self.result = None
        self.available_programs = {}

    def add_program(self, program_id):
        self.available_programs[program_id] = True

    def send_signal(self, program_id):
        if self.available_programs[program_id]:
            self.available_programs[program_id] = False
            return self.result
        return None

    def update(self):
        self.result = random.choice(self.choice)
        for key in self.available_programs:
            self.available_programs[key] = True
        return self.result


class Program:

    def __init__(self, signal):
        self.r_signal = signal
        self.program_id = uuid.uuid4()
        signal.add_program(self.program_id)

    def signal(self):
        return self.r_signal.send_signal(self.program_id)


if __name__ == "__main__":
    s = RandomSignal()
    p1 = Program(signal=s)
    p2 = Program(signal=s)

    while True:
        s.update()
        p1.signal()
        p2.signal()
        p1.signal()
        p2.signal()
        p2.signal()
        time.sleep(0.9)

