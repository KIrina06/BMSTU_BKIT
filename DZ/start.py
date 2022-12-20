from flask import Flask, render_template
import jupyter
import math

app = Flask(__name__)

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

@app.route('/<int:n>')
def index(n):
    if n >= 0:
        return str(list(use_generator(n)))

    else:
        return str(list(use_generator(n)))



if __name__ == '__main__':
    app.run(debug=True)