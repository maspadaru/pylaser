#!/bin/bash

# Benchmarking for thesis: ARES - vs Laser.py

LARS_DATA_DIR=../starbench/benchmark/data/lars

echo "============= 1. LARS - formulas ============="
pypy bench.py ATOM  0 $LARS_DATA_DIR/seq_1k_1k_1_2.stream  
pypy bench.py BOX  32 $LARS_DATA_DIR/seq_1k_1k_1_2.stream  
pypy bench.py DIA  32 $LARS_DATA_DIR/seq_1k_1k_1_2.stream  

echo "============= 2. LARS - conjunction ============="
pypy bench.py CONJ2  0 $LARS_DATA_DIR/seq_1k_1k_2_2.stream 
pypy bench.py CONJ4  0 $LARS_DATA_DIR/seq_1k_1k_4_2.stream 
pypy bench.py CONJ8  0 $LARS_DATA_DIR/seq_1k_1k_8_2.stream 
pypy bench.py CONJNOCOM  0 $LARS_DATA_DIR/seq_10_100_2_2.stream 
#pypy bench.py CONJTRAN  0 $LARS_DATA_DIR/seq_10_100_2_2.stream 


echo "============= 3. LARS - Window Size ============="
pypy bench.py SNOW  8 $LARS_DATA_DIR/seq_1k_1k_2_2.stream 
pypy bench.py SNOW 16 $LARS_DATA_DIR/seq_1k_1k_2_2.stream 
pypy bench.py SNOW 32 $LARS_DATA_DIR/seq_1k_1k_2_2.stream
pypy bench.py SNOW 64 $LARS_DATA_DIR/seq_1k_1k_2_2.stream

echo "============= 4. LARS - Flow Rate ============="
pypy bench.py SNOW 32 $LARS_DATA_DIR/seq_1k_100_2_2.stream 
pypy bench.py SNOW 32 $LARS_DATA_DIR/seq_1k_1k_2_2.stream  
pypy bench.py SNOW 32 $LARS_DATA_DIR/seq_1k_10k_2_2.stream 

# =====================================================================

echo "============= X. LARS - Math ============="
pypy bench.py ALGB  0 $LARS_DATA_DIR/seq_100_100_1_2.stream  
pypy bench.py COND  0 $LARS_DATA_DIR/seq_100_100_1_2.stream  

echo "============= XX. Types of programs ============="
pypy bench.py PROB 64 $LARS_DATA_DIR/seq_100_1k_2_2.stream
pypy bench.py TRFC 64 $LARS_DATA_DIR/seq_100_1k_2_2.stream
pypy bench.py SNOW 64 $LARS_DATA_DIR/seq_100_1k_2_2.stream

