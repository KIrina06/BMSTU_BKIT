from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный класс «Геометрическая фигура»
    """
    def pr(self):
        print("Лалалала")

    def prdecorator(self):
        print("Сейчас буду запускать функцию pr")
        pr()
        print("Выполнил фунцкию pr ")

    @abstractmethod
    def square(self):
        """
        содержит виртуальный метод для вычисления площади фигуры.
        """
        pass
