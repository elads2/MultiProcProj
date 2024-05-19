import os
import subprocess 


class ParseOutput:
    def __init__(self, output_text: str):
        self.output_text = output_text
        lines = self.output_text


CLASS_TYPES = ['S', 'W', 'A', 'B', 'C', 'D', 'E', 'F']


def run_cpu(class_type: str):
    """
    Run original version on CPU
    """
    subprocess.call(['./../q_cpu.sh', 'run_cpu.sh', f'class_type={class_type}'])
    
def run_cpu_improved(class_type: str):
    """
    Run version improved fro CPU
    """
    subprocess.call(['./../q_cpu.sh', 'run_cpu_improved.sh', f'class_type={class_type}'])
    
    
def main():
    os.chdir('runs')
    run_cpu('S')
    # parse_output = ParseOutput()
    # run_cpu('A')
    # run_cpu('B')
    

if __name__ == '__main__':
    main()
    