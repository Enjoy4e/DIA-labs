from time import time, sleep
from contextlib import contextmanager


class cm_timer_1():

    def init(self):
        self.timer = 0

    def __enter__(self):
        self.timing = time()

    def __exit__(self, exp_type, exp_value, traceback):
        print(time() - self.timing)


@contextmanager
def cm_timer_2():
    timer = time()
    yield
    print(time() - timer)


if __name__ == "__main__":
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)