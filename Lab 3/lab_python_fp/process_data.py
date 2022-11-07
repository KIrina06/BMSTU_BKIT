from lab_python_fp.print_result import print_result
from lab_python_fp.gen_random import gen_random



@print_result
def f1(arg) -> list:
    return sorted(list(set([i['job-name'] for i in arg])), key=lambda x: x.lower())


@print_result
def f2(arg) -> list:
    return list(filter(lambda s: (s.split())[0].lower() == 'программист', arg))


@print_result
def f3(arg) -> list:
    return list(map(lambda lst: lst + ' с опытом Python', arg))


@print_result
def f4(arg) -> list:
    return list(zip(arg, ['зарплата ' + str(i) + ' руб.' for i in gen_random(len(arg), 100000, 200000)]))


