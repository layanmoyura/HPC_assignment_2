from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

chunk_size = 1000004//size #1000004 to avoid 500000 printing twice in two ranks
chunk_start = rank*chunk_size
chunk_end = (rank+1)*chunk_size

data_chunk = np.genfromtxt('data.csv', delimiter=',', skip_header=chunk_start, max_rows=chunk_end - chunk_start)
man_data = np.genfromtxt('search_queries.txt', delimiter=',')

for i, man_row in enumerate(man_data):
    matching_indices = np.where(np.all(data_chunk == man_row, axis=1))[0]
    for match_index in matching_indices:
        global_index = chunk_start + match_index
        print("CSV file index:", global_index, "is equal with manual read index", i, "matched in rank:", rank)
