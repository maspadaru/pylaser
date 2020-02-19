import sys
import json
import timeit
import time

from stream.file_stream import FileStream
from evalunit.program import Program

OUTPUT = False 

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
    elif (prog_name == "PROB"):
        rules = [
            "".join(["prob(X1, X2) :- p(X1, X2) and q(X1, X2)"]),
            "".join(["warn(X1, X2) :- time_win(", win_size, ",0,1,diamond(prob(X1, X2)))"]),
            "".join(["error(X1, X2) :- time_win(", win_size, ",0,1,box(prob(X1, X2)))"]),
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
    throughput = (end_time * fact_count * 1.0) / elapsed_secs
    print("Endtime: %d, facts: %d, conclusions: %d" % (end_time, fact_count, conclusion_count))
    print("Evaluation time (sec) = %f" % eval_secs )
    print("Elapsed time (sec) = %f" % elapsed_secs )
    print("Throughput (facts/sec) = %f" % throughput )

def main():
    if (len(sys.argv) < 4):
        print ('Usage: python bench.py program_id win_size stream_file')
    else:
        prog_name = sys.argv[1]
        win_size = sys.argv[2]
        stream_path = sys.argv[3]
        rules = get_rules(prog_name, win_size)
        print("Running: %s, win_size: %s" % (prog_name, win_size))
        run(rules, stream_path)
        print("************************************************************")
        print("")
        print("")

if __name__ == '__main__':
    main()
