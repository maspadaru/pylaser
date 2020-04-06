import sys
import json
import timeit
import time

from stream.file_stream import FileStream
from evalunit.program import Program

def run_laser():
    start_time = 0 
    end_time = 100000 
    facts_per_timepoint = 1 
    is_output_enabled = False 
    s = FileStream("/home/mike/stream_file.txt", facts_per_timepoint, start_time, end_time)

    rules_atoms = [
        "q(X, Y, Z)   :- a(X, Y, Z)",
        "r(Y) :- c (X, Y)",
        "t(Y,X) :- d(X,Y)",
        "u(X,X) :- f(X)",
        "v(X, Y, X, Y) :- e(X,Y)",
    ]

    rules_all = [
        # "q(X, Y, Z, T)   :- @(T, a(X, Y, Z))",
        "r(X, Z) :- c(X,Y) and d(Y, Z)",
        # "t(X) :- time_win(5,0,1,diamond(u(X,X)))",
        "u(X,X) :- time_win(3, 0, 1, box(f(X)))",
        "v(X, Y, X, Y) :- e(X,Y)",
        "q(X, Y, Z)   :- time_win(5,0,1,diamond(a(X, Y, Z)))",
    ]

    tList = list()
    prog = Program(rules_atoms, s)
        
    for t in range(start_time, end_time + 1):
            # print("*************************** %d *********************************" % t)
            start = time.clock()
            res, tuples = prog.evaluate(t)
            if (is_output_enabled):
                print(tuples)
            end = time.clock()
            sys.stdout.write("Time = %d\r" % (t))
            sys.stdout.flush()
            tList.append(end - start)
    print("Avg = %f seconds for %d triples (%f seconds per triple)!" % (float(sum(tList)) / len(tList), facts_per_timepoint, (float(sum(tList) / len(tList) / facts_per_timepoint))))
    print("************************************************************")

def main():
    run_laser()

if __name__ == '__main__':
    main()
