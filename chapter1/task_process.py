import time
import multiprocessing

def task_a():
    print("Starting Process Task A (5 seconds)")
    time.sleep(5)
    print("Process Task A completed")

def task_b():
    print("Starting Process Task B (10 seconds)")
    time.sleep(10)
    print("Process Task B completed")

def task_c():
    print("Starting Process Task C (15 seconds)")
    time.sleep(15)
    print("Process Task C completed")

if __name__ == "__main__":
    start_time = time.time()
    
    p1 = multiprocessing.Process(target=task_a)
    p1.start()
    p1.join()
    
    p2 = multiprocessing.Process(target=task_b)
    p2.start()
    p2.join()
    
    p3 = multiprocessing.Process(target=task_c)
    p3.start()
    p3.join()
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Sequential multiprocessing total time: {total_time:.2f} seconds")
