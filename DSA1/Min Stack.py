class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.ms[-1] if self.ms else val)
        self.ms.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]
