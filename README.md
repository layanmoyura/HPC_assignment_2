### HPC_inclass

Write a simple MPI program to solve the following problem using the concepts you learnt in the class. You have 1 hour to solve each problem. 

1. There is a dataset stored in a file or files. The data stored in these files contain CSV format data. 

Each line in this CSV file contains 20 columns of int32 type. You can assume that the data stored in the files are 

Randomly generated where the values are between 0, 100. There will be 1,000,000 total number of records.

Your objective is to locate a record (that record can be randomly selected from the file) using a distributed search. 

For test cases do the following, 

Extract the records in the index 0, 10, 20, 50, 100,000 and 500,000  manually and form a search query file called 

search_queries.txt. It would  contain 6 rows each with 20 columns. You should have a script to generate the data and search queries  automatically for each run. 

Explain what you have done in plain text as a comment in the code.

2. Now imagine that the records you have written are not numeric, but they are string data, what approach would you 

Suggest to solve the problem? Write a pseudo code as the solution. 



## Python

Create a virtual environment

```bash
python3 -m venv mpi_env
source mpi_env/bin/activate
pip install mpi4py
```


## Run seacrh program 


```bash
./3397_inclass.sh
```

script used to generate data.csv and search_queries.txt also included and run from above bash script

##Solution for 2nd part

We can use hash tables when dealing with strings.

def hash_function(string_record):
    hash_value = 0
    for character in string_record:
        hash_value = hashing(character)
    return hash_value

def search(query):
    hash_value = hash_function(query)
    index = hash_table[hash_value]
    if index is not None:
        return index
    else:
        return -1

This pseudo code initally defines a hash function that take a string record as input and return a hash value. Next, The hash value is used to look up the record in the hash table. If the record is found in the hash table then the index of the record is returned. Otherwise, -1 is returned.
