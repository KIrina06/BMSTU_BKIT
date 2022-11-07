from time import sleep
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.process_data import f1, f2, f3, f4
from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort
from lab_python_fp.print_result import print_result, test_1, test_2, test_3, test_4
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
import json
import sys

try:
    path = sys.argv[1]
    print(path)
except:
    path = 'data_light.json'


def main():
    print("Task 1")
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
    print("________________________________________________________")

    print("Task 2")
    print(gen_random(5, 0, 3))
    print("________________________________________________________")

    print("Task 3")
    #data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    #data = gen_random(10, 1, 3)
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    res = Unique(data, False)
    try:
        while True:
            print(res.__next__())
    except StopIteration:
        print("StopInteration")

    print("________________________________________________________")

    print("Task 4")
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    sort(data)
    print("________________________________________________________")

    print("Task 5")
    print_result(test_1())
    print_result(test_2())
    print_result(test_3())
    print_result(test_4())
    print("________________________________________________________")

    print("Task 6")
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)
    print("________________________________________________________")

    print("Task 7")
    with open(path, "rb") as f:
        data = json.load(f)
    with cm_timer_1():
        f4(f3(f2(f1(data))))
    print("________________________________________________________")


if __name__ == '__main__':
    main()
