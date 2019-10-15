#!/bin/bash

# I Benchmark atomic formulas - variable arity

# II. Benchmark Conjunction - variable number of terms

# 1.1 Length of stream 
#pypy bench.py ATM2 100 1000 0 ../data/stream_1k_100k_1_2.txt  
#pypy bench.py ATM2 1000 1000 0 ../data/stream_1k_100k_1_2.txt  
#pypy bench.py ATM2 10000 1000 0 ../data/stream_1k_100k_1_2.txt 
#pypy bench.py ATM2 100000 1000 0 ../data/stream_1k_100k_1_2.txt  

# 1.3 Flow rate
#pypy bench.py ATM2 1000 100 0 ../data/stream_1k_100k_1_2.txt 
#pypy bench.py ATM2 1000 1000 0 ../data/stream_1k_100k_1_2.txt  
#pypy bench.py ATM2 1000 10000 0 ../data/stream_1k_100k_1_2.txt 
#pypy bench.py ATM2 1000 100000 0 ../data/stream_1k_100k_1_2.txt 

# 1.1 Predicate arity
#pypy bench.py ATM1 1000 10000 0 ../data/stream_1k_10k_1_1.txt  
#pypy bench.py ATM2 1000 10000 0 ../data/stream_1k_10k_1_2.txt 
#pypy bench.py ATM3 1000 10000 0 ../data/stream_1k_10k_1_4.txt  
#pypy bench.py ATM4 1000 10000 0 ../data/stream_1k_10k_1_8.txt  

# 1.4. Number of rules 
#pypy bench.py ATM5 1000 1000 0 ../data/stream_1k_1k_2_2.txt  
#pypy bench.py ATM6 1000 1000 0 ../data/stream_1k_1k_4_2.txt 
#pypy bench.py ATM7 1000 1000 0 ../data/stream_1k_1k_8_2.txt 

# 2. Benchmark Conjunction 

# 2.1 Number of terms
#pypy bench.py CON1 1000 1000 0 ../data/stream_1k_1k_2_2.txt  
#pypy bench.py CON2 1000 1000 0 ../data/stream_1k_1k_3_2.txt 
#pypy bench.py CON3 1000 1000 0 ../data/stream_1k_1k_4_2.txt  

# 3. Benchmarking windows and modal operators

# 3.1 Diamond
#pypy bench.py WIN1 1000 1000 3 ../data/stream_1k_100k_1_2.txt 
#pypy bench.py WIN1 1000 1000 9 ../data/stream_1k_100k_1_2.txt 
#pypy bench.py WIN1 1000 1000 27 ../data/stream_1k_100k_1_2.txt

# 3.2 Box
#pypy bench.py WIN2 1000 1000 3 ../data/stream_1k_1k_1_2.txt
#pypy bench.py WIN2 1000 1000 9 ../data/stream_1k_1k_1_2.txt
#pypy bench.py WIN2 1000 1000 27 ../data/stream_1k_1k_1_2.txt


# 4. Benchmarking for paper: Laser++ - vs Laser.py

# 4.1 Window Size 
prun -np 1 pypy bench.py PS2 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_2.txt 
prun -np 1 pypy bench.py PS2 1000 1000 9 /var/scratch/msu270/data/stream_1k_1k_2_2.txt 
prun -np 1 pypy bench.py PS2 1000 1000 27 /var/scratch/msu270/data/stream_1k_1k_2_2.txt

# 4.2 Predicate Arity 
prun -np 1 pypy bench.py PS1 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_1.txt  
prun -np 1 pypy bench.py PS2 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_2.txt 
prun -np 1 pypy bench.py PS4 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_4.txt  
prun -np 1 pypy bench.py PS8 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_8.txt  

# 4.3 Flow rate
prun -np 1 pypy bench.py PS2 1000 100 3 /var/scratch/msu270/data/stream_1k_100_2_2.txt 
prun -np 1 pypy bench.py PS2 1000 1000 3 /var/scratch/msu270/data/stream_1k_1k_2_2.txt  
prun -np 1 pypy bench.py PS2 1000 10000 3 /var/scratch/msu270/data/stream_1k_10k_2_2.txt 
prun -np 1 pypy bench.py PS2 1000 100000 3 /var/scratch/msu270/data/stream_1k_100k_2_2.txt 

