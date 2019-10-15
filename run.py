import sys
import json
import timeit

from stream.teststream import TestStream
from evalunit.program import Program

def test_diamond():
    stream = {
            0:[""],
            1:["f(x1)"],
            2:["a(x2)"],
            3:["f(x3)"],
            4:[""],
            5:["f(x5)", "f(y5)"],
            6:[""],
            7:["f(z)", "f(z)", "f(z)"],
            8:["f(z)"],
            9:[""],
            10:[""],
            11:[""],
            12:[""],
            13:[""],
            14:[""],
    }

    rules = [
            "u(X) :- tuple_win(1, diamond(f(X)))",
    ]

    s = TestStream(stream, 0,14)
    prog = Program(rules, s)

    res, tuples = prog.evaluate(0)
    print(tuples)

    res, tuples = prog.evaluate(1)
    print(tuples)
    # self.assertEquals(tuples, {1: set(['q(c,d)', 's(a)', 'z(d,c)'])})

    res, tuples = prog.evaluate(2)
    print(tuples)
    res, tuples = prog.evaluate(3)
    print(tuples)
    res, tuples = prog.evaluate(4)
    print(tuples)
    res, tuples = prog.evaluate(5)
    print(tuples)
    res, tuples = prog.evaluate(6)
    print(tuples)
    res, tuples = prog.evaluate(7)
    print(tuples)
    res, tuples = prog.evaluate(8)
    print(tuples)
    res, tuples = prog.evaluate(9)
    print(tuples)
    res, tuples = prog.evaluate(10)
    print(tuples)
    res, tuples = prog.evaluate(11)
    print(tuples)
    res, tuples = prog.evaluate(12)
    print(tuples)
    res, tuples = prog.evaluate(13)
    print(tuples)
    res, tuples = prog.evaluate(14)
    print(tuples)

def test_box():
    stream = {
            0:[""],
            1:["f(x)"],
            2:["f(x)"],
            3:["f(x)"],
            4:["f(y)"],
            5:["f(x)", "f(y)", "f(a)", "a(x)", "a(y)", "a(z)", "a(t)"],
            6:["f(y)"],
            7:["f(z)", "f(z)", "f(z)"],
            8:["f(z)"],
            9:[""],
            10:["f(a)"],
            11:["f(a)"],
            12:[""],
            13:["f(a)"],
            14:[""],
    }

    rules = [
            "u(X) :- tuple_win(3, box(f(X)))",
    ]

    s = TestStream(stream, 0,14)
    prog = Program(rules, s)

    res, tuples = prog.evaluate(0)
    print(tuples)

    res, tuples = prog.evaluate(1)
    print(tuples)
    # self.assertEquals(tuples, {1: set(['q(c,d)', 's(a)', 'z(d,c)'])})

    res, tuples = prog.evaluate(2)
    print(tuples)
    res, tuples = prog.evaluate(3)
    print(tuples)
    res, tuples = prog.evaluate(4)
    print(tuples)
    res, tuples = prog.evaluate(5)
    print(tuples)
    res, tuples = prog.evaluate(6)
    print(tuples)
    res, tuples = prog.evaluate(7)
    print(tuples)
    res, tuples = prog.evaluate(8)
    print(tuples)
    res, tuples = prog.evaluate(9)
    print(tuples)
    res, tuples = prog.evaluate(10)
    print(tuples)
    res, tuples = prog.evaluate(11)
    print(tuples)
    res, tuples = prog.evaluate(12)
    print(tuples)
    res, tuples = prog.evaluate(13)
    print(tuples)
    res, tuples = prog.evaluate(14)
    print(tuples)

def test_recursive():
    stream = {
            0:["q(1)", "p(1)"],
            1:["p(1)"],
            2:["p(1)", "q(1)"],
            3:[""],
            4:[""],
            5:[""],
            6:[""],
            7:[""],
            8:[""],
            9:[""],
            10:[""],
            11:[""],
            12:[""],
            13:[""],
            14:[""],
    }

    rules = [
            "a(X) :- b(X), c(X)",
            "b(X) :- tuple_win(3, diamond(d(X)))",
            "c(X) :- tuple_win(3, box(e(X)))",
            "e(X) :- b(X), p(X)",
            "d(X) :- q(X), p(X)",
    ]

    s = TestStream(stream, 0,14)
    prog = Program(rules, s)

    res, tuples = prog.evaluate(0)
    print(tuples)

    res, tuples = prog.evaluate(1)
    print(tuples)
    # self.assertEquals(tuples, {1: set(['q(c,d)', 's(a)', 'z(d,c)'])})

    res, tuples = prog.evaluate(2)
    print(tuples)
    res, tuples = prog.evaluate(3)
    print(tuples)
    res, tuples = prog.evaluate(4)
    print(tuples)
    res, tuples = prog.evaluate(5)
    print(tuples)
    res, tuples = prog.evaluate(6)
    print(tuples)
    res, tuples = prog.evaluate(7)
    print(tuples)
    res, tuples = prog.evaluate(8)
    print(tuples)
    res, tuples = prog.evaluate(9)
    print(tuples)
    res, tuples = prog.evaluate(10)
    print(tuples)
    res, tuples = prog.evaluate(11)
    print(tuples)
    res, tuples = prog.evaluate(12)
    print(tuples)
    res, tuples = prog.evaluate(13)
    print(tuples)
    res, tuples = prog.evaluate(14)
    print(tuples)

def test_atoms():
    stream = {
            0:["p(x0)", "q(y0, z0)", "r(z0, z0)"],
            1:["p(x1)"],
            2:["p(x2)", "q(y2, z2)"],
            3:["q(y3, z3)", "r(z3, z3)", "r(a3, z3)"],
            4:["q(y41, z41)", "q(y42, z42)"],
            5:["p(x51)", "p(x52)"],
            6:["p(x61)", "p(x62)", "q(y61, z61)", "q(y62, z62)"],
            7:[""],
            8:[""],
            9:[""],
            10:[""],
            11:[""],
            12:[""],
            13:[""],
            14:[""],
    }

    rules = [
            # "a(X, Z) :- p(X), q(Y, Z)",
            "b(X, X) :- p(X)",
            "c(Z, Y) :- q(Y, Z)",
            "d(Z) :- q(Y, Z)",
            "f(Z) :- r(Z, Z)",
    ]

    s = TestStream(stream, 0,14)
    prog = Program(rules, s)

    res, tuples = prog.evaluate(0)
    print(tuples)

    res, tuples = prog.evaluate(1)
    print(tuples)
    # self.assertEquals(tuples, {1: set(['q(c,d)', 's(a)', 'z(d,c)'])})

    res, tuples = prog.evaluate(2)
    print(tuples)
    res, tuples = prog.evaluate(3)
    print(tuples)
    res, tuples = prog.evaluate(4)
    print(tuples)
    res, tuples = prog.evaluate(5)
    print(tuples)
    res, tuples = prog.evaluate(6)
    print(tuples)
    res, tuples = prog.evaluate(7)
    print(tuples)
    res, tuples = prog.evaluate(8)
    print(tuples)
    res, tuples = prog.evaluate(9)
    print(tuples)
    res, tuples = prog.evaluate(10)
    print(tuples)
    res, tuples = prog.evaluate(11)
    print(tuples)
    res, tuples = prog.evaluate(12)
    print(tuples)
    res, tuples = prog.evaluate(13)
    print(tuples)
    res, tuples = prog.evaluate(14)
    print(tuples)


def test_transitive():
    stream = {
            0:["p(a1, a2)", "p(a2, a3)"],
            1:["p(b1,b2)", "p(b2, b3)", "p(b3, b4)"],
            2:["p(c1,c2)", "p(c2, c3)", "p(c3, c4)", "p(c4, c5)", "p(c5, c6)"],
            3:[""],
            4:[""],
            5:[""],
            6:[""],
            7:[""],
            8:[""],
            9:[""],
            10:[""],
            11:[""],
            12:[""],
            13:[""],
            14:[""],
    }

    rules = [
            "p(X, Z) :- p(X, Y) and p(Y, Z)"
    ]

    s = TestStream(stream, 0,14)
    prog = Program(rules, s)

    res, tuples = prog.evaluate(0)
    print(tuples)

    res, tuples = prog.evaluate(1)
    print(tuples)
    res, tuples = prog.evaluate(2)
    print(tuples)
    res, tuples = prog.evaluate(3)
    print(tuples)
    res, tuples = prog.evaluate(4)
    print(tuples)
    res, tuples = prog.evaluate(5)
    print(tuples)
    res, tuples = prog.evaluate(6)
    print(tuples)
    res, tuples = prog.evaluate(7)
    print(tuples)
    res, tuples = prog.evaluate(8)
    print(tuples)
    res, tuples = prog.evaluate(9)
    print(tuples)
    res, tuples = prog.evaluate(10)
    print(tuples)
    res, tuples = prog.evaluate(11)
    print(tuples)
    res, tuples = prog.evaluate(12)
    print(tuples)
    res, tuples = prog.evaluate(13)
    print(tuples)
    res, tuples = prog.evaluate(14)
    print(tuples)

def main():
    # print("Diamond")
    # test_diamond()
    # print("\n")

    # print("Box")
    # test_box()
    # print("\n")

    # print("Recursive")
    # test_recursive()
    # print("\n")

    # print("Atoms")
    # test_atoms()
    # print("\n")

    print("Transitive")
    # test_transitive()
    print("\n")

if __name__ == '__main__':
    main()
