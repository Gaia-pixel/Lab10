from dataclasses import dataclass

@dataclass
class Border:

    def __init__(self, state1no, state2no):
        self.state1no = state1no
        self.state2no = state2no

    def __str__(self):
        return f'border: {self.state1no}-{self.state2no}'