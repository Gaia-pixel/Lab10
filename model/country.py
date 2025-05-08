from dataclasses import dataclass

@dataclass
class Country:

    def __init__(self, StateAbb: str , CCode: int, StateNme: str):
        self.StateAbb = StateAbb
        self.CCode = CCode
        self.StateNme = StateNme

    def __str__(self):
        return f"{self.StateNme}"

    def __hash__(self):
        return hash(self.CCode)
