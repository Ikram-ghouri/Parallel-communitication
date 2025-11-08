from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("my rank is:", rank)

# Process 9 sends to Process 4
if rank == 9:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print(f"sending data {data} to process {destination_process}")

# Process 1 sends to Process 8
if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print(f"sending data {data} to process {destination_process}")

# Process 4 receives from Process 9
if rank == 4:
    data = comm.recv(source=9)
    print(f"data received is = {data}")

# Process 8 receives from Process 1
if rank == 8:
    data = comm.recv(source=1)
    print(f"data received is = {data}")
