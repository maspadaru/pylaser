#!/bin/bash

# Benchmarking for thesis: Laser++ - vs Laser.py

echo "============= 1. LARS - formulas ============="
pypy bench.py ATOM  0 ../data/stream_1k_1k_1_2.txt  
pypy bench.py CONJ  0 ../data/stream_1k_1k_2_2.txt 
pypy bench.py DIA  32 ../data/stream_1k_1k_1_2.txt  
pypy bench.py BOX  32 ../data/stream_1k_1k_1_2.txt  

echo "============= 2. LARS - Math ============="
pypy bench.py COMP  0 ../data/stream_1k_1k_1_2.txt  

#echo "============= 3. LARS - Laser++ Window Size ============="
#pypy bench.py PROB  8 ../data/stream_1k_1k_2_2.txt 
#pypy bench.py PROB 16 ../data/stream_1k_1k_2_2.txt 
#pypy bench.py PROB 32 ../data/stream_1k_1k_2_2.txt
#pypy bench.py PROB 64 ../data/stream_1k_1k_2_2.txt

#echo "============= 4. LARS - Flow Rate ============="
#pypy bench.py PROB 32 ../data/stream_10_100_2_2.txt 
#pypy bench.py PROB 32 ../data/stream_10_1k_2_2.txt  
#pypy bench.py PROB 32 ../data/stream_10_10k_2_2.txt 
#pypy bench.py PROB 32 ../data/stream_10_100k_2_2.txt 

# =====================================================================

#echo "============= XX. Types of programs ============="
pypy bench.py PROB 64 ../data/stream_1k_1k_2_2.txt
pypy bench.py SNOW 64 ../data/stream_1k_1k_2_2.txt
pypy bench.py TRFC 64 ../data/stream_1k_1k_2_2.txt

# Misc
#pypy bench.py ALGB  0 ../data/stream_1k_1k_1_2.txt  

# Correctness check
#pypy bench.py ALGB  0 ../data/stream_3_6_1_2.txt  
#pypy bench.py COMP  0 ../data/stream_3_6_1_2.txt  
#pypy bench.py PROB 64 ../data/stream_3_6_2_2.txt
#pypy bench.py SNOW 64 ../data/stream_3_6_2_2.txt
#pypy bench.py TRFC 64 ../data/stream_3_6_2_2.txt
