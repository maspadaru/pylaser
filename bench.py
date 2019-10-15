import sys
import json
import timeit
import time

from stream.file_stream import FileStream
from evalunit.program import Program

OUTPUT = False 

def get_rules(prog_name, win_size):
    rules = []
    if (prog_name == "ATM1"):
        rules = [
            "a(X) :- p(X)",
        ]
    elif (prog_name == "ATM2"):
        rules = [
            "a(X,Y) :- p(X,Y)",
        ]
    elif (prog_name == "ATM3"):
        rules = [
            "a(W,X,Y,Z) :- p(W,X,Y,Z)",
        ]
    elif (prog_name == "ATM4"):
        rules = [
            "a(A, B, C, D, E, F, G, H) :- p(A, B, C, D, E, F, G, H)",
        ]
    elif (prog_name == "ATM5"):
        rules = [
            "a(X, Y) :- p(X, Y)",
            "b(X, Y) :- q(X, Y)",
        ]
    elif (prog_name == "ATM6"):
        rules = [
            "a(X, Y) :- p(X, Y)",
            "b(X, Y) :- q(X, Y)",
            "c(X, Y) :- r(X, Y)",
            "d(X, Y) :- s(X, Y)",
        ]
    elif (prog_name == "ATM7"):
        rules = [
            "a(X, Y) :- p(X, Y)",
            "b(X, Y) :- q(X, Y)",
            "c(X, Y) :- r(X, Y)",
            "d(X, Y) :- s(X, Y)",
            "e(X, Y) :- t(X, Y)",
            "f(X, Y) :- u(X, Y)",
            "g(X, Y) :- v(X, Y)",
            "h(X, Y) :- w(X, Y)",
        ]
    elif (prog_name == "CON1"):
        rules = [
            "a(X,Y) :- p(X, Y) and q(X, Y)",
        ]
    elif (prog_name == "CON2"):
        rules = [
            "a(X,Y) :- p(X,Y) and q(X, Y) and r(X, Y)",
        ]
    elif (prog_name == "CON3"):
        rules = [
            "a(X,Y) :- p(X,Y) and q(X, Y) and r(X, Y) and s(X, Y)",
        ]
    elif (prog_name == "WIN1"):
        rules = [
            "".join(["a(X, Y) :- time_win(", win_size, ",0,1,diamond(p(X, Y)))"]),
        ]
    elif (prog_name == "WIN2"):
        rules = [
            "".join(["a(X, Y) :- time_win(", win_size, ",0,1,box(p(X, Y)))"]),
        ]
    elif (prog_name == "PS1"):
        rules = [
            "".join(["prob(X) :- p(X) and time_win(", win_size, ",0,1,box(q(X)))"]),
            "".join(["warn(X) :- time_win(", win_size, ",0,1,diamond(prob(X)))"]),
            "".join(["error(X) :- time_win(", win_size, ",0,1,box(prob(X)))"]),
        ]
    elif (prog_name == "PS2"):
        rules = [
            "".join(["prob(X1, X2) :- p(X1, X2) and time_win(", win_size, ",0,1,box(q(X1, X2)))"]),
            "".join(["warn(X1, X2) :- time_win(", win_size, ",0,1,diamond(prob(X1, X2)))"]),
            "".join(["error(X1, X2) :- time_win(", win_size, ",0,1,box(prob(X1, X2)))"]),
        ]
    elif (prog_name == "PS4"):
        rules = [
            "".join(["prob(X1, X2, X3, X4) :- p(X1, X2, X3, X4) and time_win(", win_size, ",0,1,box(q(X1, X2, X3, X4)))"]),
            "".join(["warn(X1, X2, X3, X4) :- time_win(", win_size, ",0,1,diamond(prob(X1, X2, X3, X4)))"]),
            "".join(["error(X1, X2, X3, X4) :- time_win(", win_size, ",0,1,box(prob(X1, X2, X3, X4)))"]),
        ]
    elif (prog_name == "PS8"):
        rules = [
            "".join(["prob(X1, X2, X3, X4, X5, X6, X7, X8) :- p(X1, X2, X3, X4, X5, X6, X7, X8) and time_win(", win_size, ",0,1,box(q(X1, X2, X3, X4, X5, X6, X7, X8)))"]),
            "".join(["warn(X1, X2, X3, X4, X5, X6, X7, X8) :- time_win(", win_size, ",0,1,diamond(prob(X1, X2, X3, X4, X5, X6, X7, X8)))"]),
            "".join(["error(X1, X2, X3, X4, X5, X6, X7, X8) :- time_win(", win_size, ",0,1,box(prob(X1, X2, X3, X4, X5, X6, X7, X8)))"]),
        ]
    return rules 


def run(rules, stream_file, end_time, fact_count):
    s = FileStream(stream_file, fact_count, 0, end_time)
    prog = Program(rules, s)
    start = time.time()
    for t in range(end_time + 1):
            res, tuples = prog.evaluate(t)
            if (OUTPUT):
                print(tuples)
    end = time.time()
    elapsed_secs = end - start
    eval_secs = prog.get_eval_secs()
    throughput = (end_time * fact_count * 1.0) / elapsed_secs
    print("Evaluation time (sec) = %f" % eval_secs )
    print("Elapsed time (sec) = %f" % elapsed_secs )
    print("Throughput (facts/sec) = %f" % throughput )

def main():
    if (len(sys.argv) < 6):
        print ('Usage: python bench.py program_id end_time fact_count win_size stream_file')
    else:
        prog_name = sys.argv[1]
        end_time = int(sys.argv[2])
        fact_count = int(sys.argv[3])
        win_size = sys.argv[4]
        stream_path = sys.argv[5]
        rules = get_rules(prog_name, win_size)
        print ("Run %s" % prog_name)
        print("timepoints: %d, fact_count: %d, win_size: %s" % (end_time, \
            fact_count, win_size))
        run(rules, stream_path, end_time, fact_count)
        print("************************************************************")
        print("")
        print("")

if __name__ == '__main__':
    main()
