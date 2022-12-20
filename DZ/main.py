import math
import start

def createF(n):
    fi = (1 + math.sqrt(5)) / 2
    Fn = int((pow(fi, n) - pow(0 - fi, 0 - n)) / (2 * fi - 1))
    return Fn

def use_generator(n):
    if n > 0:
        return (createF(x) for x in range(n))
    elif n == 0:
        return [0]
    else:
        return (createF(x) for x in range(0, n, -1))

def main():
    n = int(input())
    #print(list(use_generator(n)))
    app.run(n)


if __name__ == '__main__':
    main()