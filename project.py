<<<<<<< HEAD
#!/bin/python3
=======
#! python3

>>>>>>> cb0dbb19b718540e538412bae1dde83f122b7d16
import os
import subprocess
from pathlib import Path
from enum import Enum

RUN_TIME_STRING = 'Time in seconds'
VERIFICATION_STRING = ' Verification    ='


class RunType(Enum):
    RUN_CPU = 'sp'
    RUN_CPU_IMPROVED = 'sp_improved'
    RUN_GPU = 'sp_gpu'
    RUN_CPU_CLEAN = 'sp_cpu_clean'


CLASS_TYPES = ['S', 'W', 'A', 'B', 'C', 'D', 'E', 'F']
NPB_PATH = Path('NPB-CPP')
BINS_PATH = NPB_PATH.joinpath('bin')


def remove_bin(class_type: str):
    bin_path = BINS_PATH.joinpath(f'sp.{class_type}')
    if bin_path.exists():
        bin_path.unlink()


def run_benchmark(sp_type: str, class_type: str, num_threads: int, is_make: bool, is_vtune: bool):
    """
    Run benchmark sh file
    """
    os.chdir(NPB_PATH)
    os.environ["OMP_NUM_THREADS"] = str(num_threads)
    if 'gpu' in sp_type:
        os.environ["OMP_TARGET_OFFLOAD"] = 'MANDATORY'
    if is_make:
        subprocess.call(['make', sp_type, f'CLASS={class_type}'])
    run_args = [f'./bin/sp.{class_type}']
    if is_vtune:
        run_args = ['vtune', '-collect', 'gpu-offload'] + run_args
    subprocess.run(run_args)
    os.chdir('..')


def get_run_duration(results: str) -> float:
    for line in results.split(os.linesep):
        if RUN_TIME_STRING in line:
            run_duration = float(line.split()[-1])
        if VERIFICATION_STRING in line:
            if 'UNSUCCESSFUL' in line:
                raise Exception('Verification was unsuccessful')
            return run_duration
    raise Exception('Run duration not found in output file')


<<<<<<< HEAD
def main():
    run_type = RunType.RUN_GPU
    class_type = 'B'
    times_to_run = 1
    num_threads = 8
    is_vtune = False

    total_run_duration = 0
    remove_bin(class_type)
    for run_index in range(times_to_run):
        if run_index == 0:
            is_make = True
        else:
            is_make = False
        run_benchmark(run_type.value, class_type, num_threads, is_make=is_make, is_vtune=is_vtune)
    #     total_run_duration += get_run_duration(get_results_path(run_type.value))
    # average_run_duration = total_run_duration / times_to_run
    # print(f"Average run duration {average_run_duration}s")
=======
def main(class_type):
    run_type = RunType.RUN_CPU_IMPROVED
    # class_type = 'S'
    times_to_run = 1
    num_threads = 100

    total_run_duration = 0
    
    os.chdir('/home/u219333/')
    os.chdir('dev')
    os.chdir('Project')
    os.chdir('MultiProcProj')
    os.chdir('runs')
    runs_pwd = os.getcwd()
    for run_index in range(times_to_run):
        run_benchmark(run_type.value, class_type, num_threads)
        os.chdir(runs_pwd)
        d = get_run_duration(get_results_path(run_type.value))
        if d is not None:
            total_run_duration += d
    average_run_duration = total_run_duration / times_to_run
    print(f"Average run duration {average_run_duration}s")
>>>>>>> cb0dbb19b718540e538412bae1dde83f122b7d16


if __name__ == '__main__':
    main('B')
    
    #for c in CLASS_TYPES:
    #    print("running class %s\n\n\n\n" % c)
    #    main(c)
