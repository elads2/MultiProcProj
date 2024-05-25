import os
import subprocess
from pathlib import Path
from enum import Enum
import time

RUN_TIME_STRING = 'Time in seconds'
VERIFICATION_STRING = ' Verification    ='


class RunType(Enum):
    RUN_CPU = 'run_cpu'
    RUN_CPU_IMPROVED = 'run_cpu_improved'
    RUN_GPU = 'run_gpu'
    RUN_CPU_CLEAN = 'run_cpu_clean'


CLASS_TYPES = ['S', 'W', 'A', 'B', 'C', 'D', 'E', 'F']
BINS_PATH = Path('NPB-CPP', 'bin')


def remove_bin(class_type: str):
    bin_path = BINS_PATH.joinpath(f'sp.{class_type}')
    if bin_path.exists():
        bin_path.unlink()


def run_benchmark(script_name: str, class_type: str, num_threads: int, is_make: bool, is_vtune: bool):
    """
    Run benchmark sh file
    """
    if 'cpu' in script_name:
        q_sub = 'cpu'
    else:
        q_sub = 'gpu'
    if is_make:
        is_make_value = 1
    else:
        is_make_value = 0
    if is_vtune:
        is_vtune_value = 1
    else:
        is_vtune_value = 0
    subprocess.call(
        [f'./../q_{q_sub}.sh',
         f'{script_name}.sh',
         f'class_type={class_type},OMP_NUM_THREADS={num_threads},is_make={is_make_value},is_vtune={is_vtune_value}'])


def get_run_duration(results_path: Path) -> float:
    with open(results_path, 'r') as results_file:
        for line in results_file.readlines():
            if RUN_TIME_STRING in line:
                run_duration = float(line.split()[-1])
            if VERIFICATION_STRING in line:
                if 'UNSUCCESSFUL' in line:
                    raise Exception('Verification was unsuccessful')
                return run_duration
    raise Exception('Run duration not found in output file')


def get_results_path(script_name: str, timeout: float = 500) -> Path:
    start_time = time.time()
    while time.time() - start_time < timeout:
        file_list = [f for f in os.listdir() if os.path.isfile(f)]
        for file_name in file_list:
            if '.o' in file_name and file_name.split('.')[0] == script_name:
                # try to make sure it can be opened
                try:
                    with open(file_name, 'r') as _:
                        pass
                    return Path(file_name)
                except PermissionError:
                    pass
    raise Exception('Results file not found')


def main():
    run_type = RunType.RUN_GPU
    class_type = 'B'
    times_to_run = 1
    num_threads = 48
    is_vtune = False

    total_run_duration = 0
    remove_bin(class_type)
    os.chdir('runs')
    runs_pwd = os.getcwd()
    for run_index in range(times_to_run):
        if run_index == 0:
            run_benchmark(run_type.value, class_type, num_threads, is_make=True, is_vtune=is_vtune)
        else:
            run_benchmark(run_type.value, class_type, num_threads, is_make=False, is_vtune=is_vtune)
        os.chdir(runs_pwd)
        total_run_duration += get_run_duration(get_results_path(run_type.value))
    average_run_duration = total_run_duration / times_to_run
    print(f"Average run duration {average_run_duration}s")


if __name__ == '__main__':
    main()
