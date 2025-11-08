import time
import threading

def task_a():
    print("Starting Thread Task A (5 seconds)")
    time.sleep(5)
    print("Thread Task A completed")

def task_b():
    print("Starting Thread Task B (10 seconds)")
    time.sleep(10)
    print("Thread Task B completed")

def task_c():
    print("Starting Thread Task C (15 seconds)")
    time.sleep(15)
    print("Thread Task C completed")

if __name__ == "__main__":
    start_time = time.time()
    
    t1 = threading.Thread(target=task_a)
    t1.start()
    t1.join()
    
    t2 = threading.Thread(target=task_b)
    t2.start()
    t2.join()
    
    t3 = threading.Thread(target=task_c)
    t3.start()
    t3.join()
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Sequential threading total time: {total_time:.2f} seconds")
