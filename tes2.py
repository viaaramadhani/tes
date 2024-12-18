# Studi Kasus Pemilihan Tugas Siswa dengan Brute Force, Greedy, dan Selection Sort
from itertools import combinations
def brute_force_task_selection(tasks, limit_waktu):

    kombinasi_terbaik = []
    max_prioritas = 0

    for r in range(1, len(tasks) + 1):
        for combination in combinations(tasks, r):
            total_waktu = sum(task['waktu'] for task in combination)
            total_prioritas = sum(task['prioritas'] for task in combination)

            if total_waktu <= limit_waktu and total_prioritas > max_prioritas:
                max_prioritas = total_prioritas
                kombinasi_terbaik = combination

    return kombinasi_terbaik

def selection_sort_tasks(tasks):

    for i in range(len(tasks)):
        max_index = i
        for j in range(i + 1, len(tasks)):
            if tasks[j]['prioritas'] > tasks[max_index]['prioritas']:
                max_index = j

        tasks[i], tasks[max_index] = tasks[max_index], tasks[i]

    return tasks

tasks = [
    {"name": "Task 1", "waktu": 2, "prioritas": 50},
    {"name": "Task 2", "waktu": 1, "prioritas": 30},
    {"name": "Task 3", "waktu": 3, "prioritas": 60},
    {"name": "Task 4", "waktu": 4, "prioritas": 40}
]

limit_waktu = 6

# Brute Force Algorithm
print("\n--- Brute Force Algorithm ---")
result = brute_force_task_selection(tasks, limit_waktu)
print("Selected Tasks:", [task['name'] for task in result])

# Selection Sort
print("\n--- Selection Sort Tasks ---")
sorted_tasks = selection_sort_tasks(tasks)
print("Sorted Tasks:", [task['name'] for task in sorted_tasks])