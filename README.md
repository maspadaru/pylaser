# Laser

## How to run the evaluations?
Before running the evaluations, please make sure that you have [Pypy JIT compiler](https://pypy.org/). 
To run the evaluations you can simply execute the following command:

```
./bench.sh
```


## Other

`bench.py` - Run benchmarks - Edit this file first to set the location of the 
input stream file.


`run.py` - Run Laser on some input hardcoded as strings in the file. Useful for 
small corectness tests.


`run_file.py` - Run Laser on some input read from a text file. The path to this
input file is hardcoded.
