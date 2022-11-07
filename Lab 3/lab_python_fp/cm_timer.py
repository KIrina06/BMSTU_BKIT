from time import time
from contextlib import contextmanager

@contextmanager
def cm_timer_1():
    start = time()
    yield None
    finish = time()
    print("Время работы: {}".format(finish - start))

class cm_timer_2:
    def __int__(self):
        self.start = 0
        self.finish = 0

    def __enter__(self):
        self.start = time()

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.finish = time()
        print("Время работы: {}".format(self.finish - self.start))
