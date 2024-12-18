# Studi Kasus Pemilihan Tugas Siswa dengan Brute Force dan Selection Sort
from itertools import combinations
import time

def brute_force(tugas, limit):
    kombinasi_terbaik, max_prioritas = [], 0
    for r in range(1, len(tugas) + 1):
        for comb in combinations(tugas, r):
            total_waktu = sum(task['waktu'] for task in comb)
            total_prioritas = sum(task['prioritas'] for task in comb)
            if total_waktu <= limit and total_prioritas > max_prioritas:
                kombinasi_terbaik, max_prioritas = comb, total_prioritas
    return kombinasi_terbaik

def selection_sort(tugas):
    for i in range(len(tugas)):
        max_idx = i
        for j in range(i + 1, len(tugas)):
            if tugas[j]['prioritas'] > tugas[max_idx]['prioritas']:
                max_idx = j
        tugas[i], tugas[max_idx] = tugas[max_idx], tugas[i]
    return tugas

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start

# Data tugas
tugas = [
    {"name": "Task 1", "waktu": 2, "prioritas": 50},
    {"name": "Task 2", "waktu": 1, "prioritas": 30},
    {"name": "Task 3", "waktu": 3, "prioritas": 60},
    {"name": "Task 4", "waktu": 4, "prioritas": 40}
]
limit_waktu = 6

# Brute Force
brute_result, brute_time = measure_time(brute_force, tugas, limit_waktu)
print("\n--- Brute Force ---")
print("Prioritas Tugas:", [t['name'] for t in brute_result], f"| Time: {brute_time:.6f} sec")

# Selection Sort
sorted_tasks, sort_time = measure_time(selection_sort, tugas.copy())
print("\n--- Selection Sort ---")
print("Prioritas Tugas:", [t['name'] for t in sorted_tasks], f"| Time: {sort_time:.6f} sec")