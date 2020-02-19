#!/bin/bash

# 1. Benchmarking for thesis: Laser++ - vs Laser.py

# 4.1 Individual formulas 
#pypy bench.py ATOM  0 ../data/stream_1k_1k_1_2.txt  
#pypy bench.py CONJ  0 ../data/stream_1k_1k_2_2.txt 
#pypy bench.py DIA  32 ../data/stream_1k_1k_1_2.txt  
#pypy bench.py BOX  32 ../data/stream_1k_1k_1_2.txt  

# 4.2 Window Size 
#pypy bench.py PROB  8 ../data/stream_1k_1k_2_2.txt 
#pypy bench.py PROB 16 ../data/stream_1k_1k_2_2.txt 
#pypy bench.py PROB 32 ../data/stream_1k_1k_2_2.txt
#pypy bench.py PROB 64 ../data/stream_1k_1k_2_2.txt

# 4.3 Flow rate
pypy bench.py PROB 32 ../data/stream_10_100_2_2.txt 
pypy bench.py PROB 32 ../data/stream_10_1k_2_2.txt  
pypy bench.py PROB 32 ../data/stream_10_10k_2_2.txt 
pypy bench.py PROB 32 ../data/stream_10_100k_2_2.txt 

