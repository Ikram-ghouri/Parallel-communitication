# Chapter 1: Sequential Processing with Threads and Processes in Python

## Overview
This chapter demonstrates sequential processing using threading and multiprocessing in Python. We simulate three tasks with durations of 5, 10, and 15 seconds to compare execution times and overhead when using threads vs processes for sequential execution.

## Files

### task_thread.py: Sequential Processing with Threading
- **Purpose**: Runs tasks one after another using `threading.Thread` (start and join sequentially for A: 5s, B: 10s, C: 15s).
- **Expected Output**:
  ```
  Starting Thread Task A (5 seconds)
  Thread Task A completed
  Starting Thread Task B (10 seconds)
  Thread Task B completed
  Starting Thread Task C (15 seconds)
  Thread Task C completed
  Sequential threading total time: 30.XX seconds
  ```
- **Total Time**: Approximately 30 seconds plus minor threading overhead.

### task_process.py: Sequential Processing with Multiprocessing
- **Purpose**: Runs tasks one after another using `multiprocessing.Process` (start and join sequentially for A: 5s, B: 10s, C: 15s).
- **Expected Output**:
  ```
  Starting Process Task A (5 seconds)
  Process Task A completed
  Starting Process Task B (10 seconds)
  Process Task B completed
  Starting Process Task C (15 seconds)
  Process Task C completed
  Sequential multiprocessing total time: 30.XX seconds
  ```
- **Total Time**: Approximately 30 seconds plus process creation overhead.

## Conclusions
- **Threading Sequential**: Similar to pure sequential but with slight overhead from thread creation/joining; useful for I/O-bound tasks but limited by GIL for CPU-bound.
- **Multiprocessing Sequential**: Similar to pure sequential but with higher overhead from process creation/joining; better for CPU-bound tasks but more resource-intensive.
- Overhead comparison: Threading has less overhead than multiprocessing for sequential execution.
- Note: For true parallelism, concurrent execution is needed; here we demonstrate sequential to highlight overhead differences.

## Screenshots
- [Placeholder: Screenshot of task_thread.py terminal output]
- [Placeholder: Screenshot of task_process.py terminal output]

Add actual screenshots after running the scripts.
