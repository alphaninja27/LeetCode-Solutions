from threading import Lock, Semaphore
class DiningPhilosophers:

    def __init__(self):
        self.l = [Lock() for _  in range(5)]
        self.b = Semaphore(4)
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.b:
            l, r = philosopher, (philosopher + 1)%5
            with self.l[l], self.l[r]:
                pickLeftFork()
                pickRightFork()
                eat()
                putRightFork()
                putLeftFork()
