import os
import random
import string
import sys


def id_generator(size: int = 10) -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))


print('------Program to append multiple .arff files using Weka------')

sys.argv.pop(0)
if len(sys.argv) < 3:
    file_extension: str = 'py'
    try:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        base_path: str = sys._MEIPASS
        file_extension = 'exe'
    except AttributeError:
        pass
    raise ValueError('Cannot append less than 2 files.\n'
                     f'Syntax: {"python " if file_extension == "py" else ""}append_multiple.{file_extension} '
                     'file1.arff file2.arff file3.arff '
                     'outputfile.arff')

print('Enter the path to installation directory of Weka or weka.jar')
print('Example: C:\\Program Files\\Weka-3-8-5')
print('Leave empty and press Enter if the program is in the installation directory')
installation_dir: str = input('Path: ').strip()
if not installation_dir == '':
    installation_dir = installation_dir.replace('\\', '/').rstrip('\\').rstrip('/') + '/'

print('Enter the path to directory containing all .arff files')
print('Example: D:\\Users\\VarunS2002\\Desktop\\Weka Datasets\\samples')
print('Leave empty and press Enter if the files are in the same directory as the program')
files_dir: str = input('Path: ').strip()
if not files_dir == '':
    files_dir = files_dir.replace('\\', '/').rstrip('\\').rstrip('/') + '/'

print('Enter the path for the output .arff file')
print('Example: D:\\Users\\VarunS2002\\Desktop\\Weka Datasets\\samples\\output')
print('Leave empty and press Enter if you want it to be in the same directory as the datasets')
output_dir: str = input('Path: ').strip()
if not output_dir == '':
    output_dir = output_dir.replace('\\', '/').rstrip('\\').rstrip('/') + '/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
else:
    output_dir = files_dir

files: list[str] = [files_dir + file_name for file_name in sys.argv]
if files_dir != output_dir:
    files[-1] = files[-1].replace(files_dir, output_dir)
temporary_files: list[str] = [files_dir + id_generator() + '.arff' for _ in range(len(files) - 2)]

for i in range(len(temporary_files)):
    if i == 0 and len(files) == 3:
        os.system(f'java -classpath "{installation_dir}weka.jar" weka.core.Instances append '
                  f'"{files[0]}" "{files[1]}" > "{files[2]}"')
    elif i == 0:
        os.system(f'java -classpath "{installation_dir}weka.jar" weka.core.Instances append '
                  f'"{files[0]}" "{files[1]}" > "{temporary_files[i]}"')
    elif i == len(temporary_files) - 1:
        os.system(f'java -classpath "{installation_dir}weka.jar" weka.core.Instances append '
                  f'"{temporary_files[i - 1]}" "{files[i + 1]}" > "{files[-1]}"')
        os.remove(temporary_files[i - 1])
    else:
        os.system(f'java -classpath "{installation_dir}weka.jar" weka.core.Instances append '
                  f'"{temporary_files[i - 1]}" "{files[i + 1]}" > '
                  f'"{temporary_files[i]}"')
        os.remove(temporary_files[i - 1])
