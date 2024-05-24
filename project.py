import os
import subprocess
from pathlib import Path
from enum import Enum
import time

RUN_TIME_STRING = 'Time in seconds'


class RunType(Enum):
    RUN_CPU = 'run_cpu'
    RUN_CPU_IMPROVED = 'run_cpu_improved'
    RUN_GPU = 'run_gpu'


CLASS_TYPES = ['S', 'W', 'A', 'B', 'C', 'D', 'E', 'F']


def run_benchmark(script_name: str, class_type: str, num_threads: int):
    """
    Run benchmark sh file
    """
    subprocess.call(['./../q_cpu.sh', f'{script_name}.sh', f'class_type={class_type},OMP_NUM_THREADS={num_threads}'])


def get_run_duration(results_path: Path) -> float:
    with open(results_path, 'r') as results_file:
        for line in results_file.readlines():
            if RUN_TIME_STRING in line:
                return float(line.split()[-1])


def get_results_path(script_name: str, timeout: float = 100) -> Path:
    start_time = time.time()
    while time.time() - start_time < timeout:
        file_list = [f for f in os.listdir() if os.path.isfile(f)]
        for file_name in file_list:
            if '.o' in file_name and file_name.split('.')[0] == script_name:
                return Path(file_name)
    raise Exception('Results file not found')


def main():
    run_type = RunType.RUN_CPU
    class_type = 'S'
    times_to_run = 1
    num_threads = 1

    total_run_duration = 0
    os.chdir('runs')
    runs_pwd = os.getcwd()
    for run_index in range(times_to_run):
        run_benchmark(run_type.value, class_type, num_threads)
        os.chdir(runs_pwd)
        total_run_duration += get_run_duration(get_results_path(run_type.value))
    average_run_duration = total_run_duration / times_to_run
    print(f"Average run duration {average_run_duration}s")


if __name__ == '__main__':
    main()
