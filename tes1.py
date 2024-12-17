# Studi Kasus Pemilihan Tugas Siswa dengan Brute Force, Greedy, dan Selection Sort
from itertools import combinations
import time

def brute_force(tasks, limit):
    return max((c for r in range(1, len(tasks)+1) for c in combinations(tasks, r) if sum(t['waktu'] for t in c) <= limit),
                key=lambda x: sum(t['prioritas'] for t in x), default=[])

def greedy(tasks, limit):
    selected, remaining = [], limit
    for t in sorted(tasks, key=lambda t: t['prioritas'] / t['waktu'], reverse=True):
        if t['waktu'] <= remaining: selected.append(t); remaining -= t['waktu']
    return selected

def selection_sort(tasks):
    for i in range(len(tasks)):
        max_idx = max(range(i, len(tasks)), key=lambda j: tasks[j]['prioritas'])
        tasks[i], tasks[max_idx] = tasks[max_idx], tasks[i]
    return tasks

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

# Data tugas
tasks = [
    {"name": "Task 1", "waktu": 2, "prioritas": 50},
    {"name": "Task 2", "waktu": 1, "prioritas": 30},
    {"name": "Task 3", "waktu": 3, "prioritas": 60},
    {"name": "Task 4", "waktu": 4, "prioritas": 40}
]
limit_waktu = 6

# Brute Force
start_brute_force = time.perf_counter()
brute_result = brute_force(tasks, limit_waktu)
end_time_brute_force = time.perf_counter()
print("\n--- Brute Force ---")
print("Tasks:", [t['name'] for t in brute_result], f"| Time: {end_time_brute_force - start_brute_force:.6f} sec")

# Greedy
greedy_result, greedy_time = measure_time(greedy, tasks, limit_waktu)
print("\n--- Greedy ---")
print("Tasks:", [t['name'] for t in greedy_result], f"| Time: {greedy_time:.6f} sec")

# Selection Sort
sorted_tasks, sort_time = measure_time(selection_sort, tasks.copy())
print("\n--- Selection Sort ---")
print("Tasks:", [t['name'] for t in sorted_tasks], f"| Time: {sort_time:.6f} sec")