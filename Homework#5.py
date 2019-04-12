import os
import shutil
import sys

# HM5 #1.1.1

path_dir = [('dir_' + str(i + 1)) for i in range(9)]


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' directory already exists')


for i in path_dir:
     make_dir(i)

# HM5 #1.1.2

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
list_dir(main_path)

# HM5 #1.1.3

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)

first_file = sys.argv[0]
backup_file = first_file + '.backup'
copy_file(first_file,backup_file)

