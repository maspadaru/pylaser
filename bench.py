import sys
import json
import timeit
import time

from stream.file_stream import FileStream
from evalunit.program import Program

OUTPUT = False 
# OUTPUT = True 

def get_rules(prog_name, win_size):
    rules = []
    if (prog_name == "ATOM"):
        rules = [
            "a(X1, X2) :- p(X1, X2)",
        ]
    elif (prog_name == "CONJ"):
        rules = [
            "a(X1,X2) :- p(X1, X2) and q(X1, X2)",
        ]
    elif (prog_name == "DIA"):
        rules = [
            "".join(["a(X1, X2) :- time_win(", win_size, ",0,1,diamond(p(X1, X2)))"]),
        ]
    elif (prog_name == "BOX"):
        rules = [
            "".join(["a(X1, X2) :- time_win(", win_size, ",0,1,box(p(X1, X2)))"]),
        ]
    elif (prog_name == "ALGB"):
        rules = [
            "a(Y) :- p(X1, X2) and MATH(+,Y,X1,99)",
        ]
    elif (prog_name == "COMP"):
        rules = [
            "a(X1, X2) :- p(X1, X2) and COMP(>=,X1,X2)",
            "b(X1, X2) :- p(X1, X2) and COMP(<=,X1,X2)",
            "c(X1, X2) :- p(X1, X2) and COMP(>,X1,X2)",
            "d(X1, X2) :- p(X1, X2) and COMP(<,X1,X2)",
        ]
    elif (prog_name == "PROB"):
        rules = [
            "".join(["warn(X1, X2) :- time_win(", win_size, ",0,1,diamond(p(X1, X2)))"]),
            "".join(["error(X1, X2) :- time_win(", win_size, ",0,1,box(q(X1, X2)))"]),
            "prob(X1, X2) :- error(X1, X2) and warn(X1, X2)",
        ]
    elif (prog_name == "SNOW"):
        rules = [
            "".join(["snow(X1, X2) :- time_win(", win_size, \
                    ",0,1,diamond(p(X1, X2))) and time_win(",\
                    win_size, ",0,1,box(q(X1, X2)))"]),
        ]
    elif (prog_name == "TRFC"):
        rules = [
            "".join(["warning(X1, X2) :- time_win(", win_size, ",0,1,diamond(p(X1, X2)))"]),
            "".join(["stop(X1, X2) :- time_win(", win_size, ",0,1,box(q(X1, X2)))"]),
            "jam(X1, X2) :- p(X1, X2) and q(X1, X2)",
        ]
    return rules 


def run(rules, stream_file):
    s = FileStream(stream_file)
    timeline = s.getTimeLine()
    end_time = timeline["endTime"]
    prog = Program(rules, s)
    fact_count = 0
    conclusion_count = 0
    start = time.time()
    for t in range(end_time + 1):
            res, tuples = prog.evaluate(t)
            for key, value in tuples.items():   
                conclusion_count += len(value)
            fact_count += s.getNumberOfTuplesAt(t)
            if (OUTPUT):
                print(tuples)
    end = time.time()
    elapsed_secs = end - start
    eval_secs = prog.get_eval_secs()
    throughput = (fact_count * 1.0) / elapsed_secs
    print("Endtime: %d" % end_time)
    print("Facts: %d, Conclusions: %d" % (fact_count, conclusion_count))
    print("Time: %f seconds" % elapsed_secs )
    print("Throughput: %f facts/sec" % throughput )

def main():
    if (len(sys.argv) < 4):
        print ('Usage: python bench.py program_id win_size stream_file')
    else:
        prog_name = sys.argv[1]
        win_size = sys.argv[2]
        stream_path = sys.argv[3]
        rules = get_rules(prog_name, win_size)
        print("Program: %s, win_size: %s" % (prog_name, win_size))
        print("Input: %s" % stream_path)
        run(rules, stream_path)
        print("************************************************************")
        print("")

if __name__ == '__main__':
    main()
