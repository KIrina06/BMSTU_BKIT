# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case, **kwargs):
        self.data = items
        self.ignore_case = ignore_case
        self.index = 0
        self.data2 = set()

        pass

    def __next__(self):
        if not self.ignore_case:
            for count, el in enumerate(self.data):
                if type(el) is str:
                    self.data[count] = el.lower()

        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index += 1
                if current not in self.data2:
                    self.data2.add(current)
                    return current
        pass

    def __iter__(self):
        return self
