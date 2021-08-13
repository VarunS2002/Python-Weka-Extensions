import os
import random
import string
import sys


def id_generator(size: int = 10) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))


sys.argv.pop(0)
if len(sys.argv) < 3:
    raise ValueError('Cannot append less than 2 files.\n'
                     'Syntax: python append_multiple.py '
                     'file1.arff file2.arff file3.arff '
                     'outputfile.arff')
files: list[str] = sys.argv
temporary_files: list[str] = [
    id_generator() + '.arff' for _ in range(len(files) - 2)]
for i in range(len(temporary_files)):
    if i == 0 and len(files) == 3:
        os.system(f'java -classpath weka.jar weka.core.Instances append '
                  f'{files[0]} {files[1]} > {files[2]}')
    elif i == 0:
        os.system(f'java -classpath weka.jar weka.core.Instances append '
                  f'{files[0]} {files[1]} > {temporary_files[i]}')
    elif i == len(temporary_files) - 1:
        os.system(f'java -classpath weka.jar weka.core.Instances append '
                  f'{temporary_files[i - 1]} {files[i + 1]} > {files[-1]}')
        os.remove(temporary_files[i - 1])
    else:
        os.system(f'java -classpath weka.jar weka.core.Instances append '
                  f'{temporary_files[i - 1]} {files[i + 1]} > '
                  f'{temporary_files[i]}')
        os.remove(temporary_files[i - 1])

